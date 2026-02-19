import pygame
import sys
import random

pygame.init()

ANCHO, ALTO = 800, 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Enemigos que disparan y cambian movimiento")

clock = pygame.time.Clock()

# --- JUGADOR ---
jugador = pygame.Rect(400, 500, 50, 50)
color_jugador = (0, 200, 255)
velocidad = 5
vidas = 3   

# --- DISPAROS JUGADOR ---
disparos = []
color_disparo = (255, 255, 0)
vel_disparo = 7

# --- DISPAROS ENEMIGOS ---
disparos_enemigos = []
color_disparo_enemigo = (255, 100, 100)
vel_disparo_enemigo = 5
PROBABILIDAD_DISPARO = 0.01

# --- ENEMIGOS ---
enemigos = []
color_enemigo = (200, 50, 50)
vel_vertical = 2
vel_horizontal = 2

for i in range(5):
    x = random.randint(50, ANCHO - 50)
    y = random.randint(50, 200)
    enemigo = {
        'rectangulo': pygame.Rect(x, y, 50, 50),
        'direccion': random.choice([-1, 1])
    }
    enemigos.append(enemigo)

contador = 0
juego_activo = True

fuente = pygame.font.SysFont(None, 40)
fuente_final = pygame.font.SysFont(None, 60)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if juego_activo:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    nuevo_disparo = pygame.Rect(jugador.centerx - 5, jugador.top - 10, 10, 20)
                    disparos.append(nuevo_disparo)

    if juego_activo:

        # --- Movimiento jugador ---
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador.left > 0:
            jugador.x -= velocidad
        if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
            jugador.x += velocidad

        # --- Movimiento enemigos ---
        for e in enemigos:
            e['rectangulo'].y += vel_vertical
            e['rectangulo'].x += e['direccion'] * vel_horizontal

            if e['rectangulo'].left <= 0 or e['rectangulo'].right >= ANCHO:
                e['direccion'] *= -1

            if e['rectangulo'].top > ALTO:
                e['rectangulo'].y = random.randint(-100, -40)
                e['rectangulo'].x = random.randint(50, ANCHO - 50)
                e['direccion'] = random.choice([-1, 1])

            # NUEVO: disparo enemigo aleatorio
            if random.random() < PROBABILIDAD_DISPARO: 
                disparo_enemigo = pygame.Rect(
                    e['rectangulo'].centerx - 5,
                    e['rectangulo'].bottom,
                    10,
                    20
                )
                disparos_enemigos.append(disparo_enemigo)

        # --- Movimiento disparos jugador ---
        for d in disparos:
            d.y -= vel_disparo
        disparos = [d for d in disparos if d.bottom > 0]

        # --- Movimiento disparos enemigos ---
        for de in disparos_enemigos:
            de.y += vel_disparo_enemigo
        disparos_enemigos = [de for de in disparos_enemigos if de.top < ALTO]

        # --- Colisiones disparos jugador-enemigos ---
        for d in disparos:
            for e in enemigos:
                if d.colliderect(e['rectangulo']):
                    disparos.remove(d)
                    enemigos.remove(e)
                    contador += 1
                    break

        # NUEVO: Colisión disparo enemigo-jugador ---
        for de in disparos_enemigos:
            if de.colliderect(jugador):
                disparos_enemigos.remove(de)
                vidas -= 1
                if vidas <= 0:
                    juego_activo = False

        # --- Colisiones enemigos-jugador ---
        for e in enemigos:
            if e['rectangulo'].colliderect(jugador):
                juego_activo = False

    # --- Dibujar ---
    screen.fill((30, 30, 30))

    if juego_activo:
        pygame.draw.rect(screen, color_jugador, jugador)

    for d in disparos:
        pygame.draw.rect(screen, color_disparo, d)

    for de in disparos_enemigos:
        pygame.draw.rect(screen, color_disparo_enemigo, de)

    for e in enemigos:
        pygame.draw.rect(screen, color_enemigo, e['rectangulo'])

    # Mostrar contador
    texto_contador = fuente.render(f"Enemigos eliminados: {contador}", True, (255, 255, 255))
    screen.blit(texto_contador, (10, 10))

    # NUEVO: mostrar vidas
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, (255, 255, 255))
    screen.blit(texto_vidas, (ANCHO - 120, 10))

    if not juego_activo:
        mensaje = fuente_final.render("¡GAME OVER!", True, (255, 0, 0))
        rect = mensaje.get_rect(center=(ANCHO // 2, ALTO // 2))
        screen.blit(mensaje, rect)
    elif juego_activo and not enemigos:
        mensaje = fuente_final.render("¡HAS GANADO!", True, (0, 255, 0))
        rect = mensaje.get_rect(center=(ANCHO // 2, ALTO // 2))
        screen.blit(mensaje, rect)
        juego_activo = False

    pygame.display.flip()
    clock.tick(60)
