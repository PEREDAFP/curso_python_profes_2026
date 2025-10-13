import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Tamaño de pantalla
ANCHO, ALTO = 800, 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rectángulo que dispara y enemigos móviles")

# Reloj
clock = pygame.time.Clock()

# --- JUGADOR ---
jugador = pygame.Rect(400, 500, 50, 50)
color_jugador = (0, 200, 255)
velocidad = 5

# --- DISPAROS ---
disparos = []
color_disparo = (255, 255, 0)
vel_disparo = 7

# --- ENEMIGOS ---
enemigos = []
color_enemigo = (200, 50, 50)
vel_vertical = 1.5
vel_horizontal = 2

for i in range(5):
    x = random.randint(50, ANCHO - 50)
    y = random.randint(50, 200)
    enemigo = pygame.Rect(x, y, 50, 50)
    # Añadimos una dirección horizontal aleatoria: 1 = derecha, -1 = izquierda
    enemigo.direccion_x = random.choice([-1, 1])
    enemigos.append(enemigo)

# Contador de enemigos eliminados
contador = 0

# Control del juego
juego_activo = True
fuente = pygame.font.SysFont(None, 40)
fuente_final = pygame.font.SysFont(None, 60)

while True:
    # --- Eventos ---
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
            # Movimiento vertical
            e.y += vel_vertical

            # Movimiento horizontal
            e.x += e.direccion_x * vel_horizontal

            # Cambiar dirección si llega a los bordes
            if e.left <= 0 or e.right >= ANCHO:
                e.direccion_x *= -1

            # Si bajan del todo, los reposicionamos arriba
            if e.top > ALTO:
                e.y = random.randint(-100, -40)
                e.x = random.randint(50, ANCHO - 50)
                e.direccion_x = random.choice([-1, 1])

        # --- Movimiento disparos ---
        for d in disparos:
            d.y -= vel_disparo
        disparos = [d for d in disparos if d.bottom > 0]

        # --- Colisiones disparos-enemigos ---
        for d in disparos[:]:
            for e in enemigos[:]:
                if d.colliderect(e):
                    disparos.remove(d)
                    enemigos.remove(e)
                    contador += 1  # aumentar contador
                    break

        # --- Colisiones enemigos-jugador ---
        for e in enemigos:
            if e.colliderect(jugador):
                juego_activo = False  # fin del juego

    # --- Dibujar ---
    screen.fill((30, 30, 30))

    # Dibujar jugador
    if juego_activo:
        pygame.draw.rect(screen, color_jugador, jugador)

    # Dibujar disparos
    for d in disparos:
        pygame.draw.rect(screen, color_disparo, d)

    # Dibujar enemigos
    for e in enemigos:
        pygame.draw.rect(screen, color_enemigo, e)

    # Mostrar contador arriba a la izquierda
    texto_contador = fuente.render(f"Enemigos eliminados: {contador}", True, (255, 255, 255))
    screen.blit(texto_contador, (10, 10))

    # Mensajes de fin de juego
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
