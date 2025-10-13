import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Tamaño de pantalla
ANCHO, ALTO = 800, 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rectángulo que dispara y enemigos")

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
vel_enemigo = 2

for i in range(5):
    x = random.randint(50, ANCHO - 50)
    y = random.randint(50, 200)
    enemigo = pygame.Rect(x, y, 50, 50)
    enemigos.append(enemigo)

# Variable para controlar si el juego sigue activo
juego_activo = True

# Fuente para mensajes
fuente = pygame.font.SysFont(None, 60)

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
        # --- Movimiento del jugador ---
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador.left > 0:
            jugador.x -= velocidad
        if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
            jugador.x += velocidad

        # --- Movimiento de enemigos ---
        for e in enemigos:
            e.y += vel_enemigo
            if e.top > ALTO:
                e.y = random.randint(-100, -40)
                e.x = random.randint(50, ANCHO - 50)

        # --- Movimiento de disparos ---
        for d in disparos:
            d.y -= vel_disparo
        disparos = [d for d in disparos if d.bottom > 0]

        # --- Colisiones disparos-enemigos ---
        for d in disparos[:]:
            for e in enemigos[:]:
                if d.colliderect(e):
                    disparos.remove(d)
                    enemigos.remove(e)
                    break

        # --- Colisiones enemigos-jugador ---
        for e in enemigos:
            if e.colliderect(jugador):
                juego_activo = False  # Fin del juego

    # --- Dibujar ---
    screen.fill((30, 30, 30))

    if juego_activo:
        pygame.draw.rect(screen, color_jugador, jugador)
        for d in disparos:
            pygame.draw.rect(screen, color_disparo, d)
        for e in enemigos:
            pygame.draw.rect(screen, color_enemigo, e)
    else:
        mensaje = fuente.render("¡GAME OVER!", True, (255, 0, 0))
        rect = mensaje.get_rect(center=(ANCHO // 2, ALTO // 2))
        screen.blit(mensaje, rect)

    # --- Ganar si no quedan enemigos ---
    if juego_activo and not enemigos:
        mensaje = fuente.render("¡HAS GANADO!", True, (0, 255, 0))
        rect = mensaje.get_rect(center=(ANCHO // 2, ALTO // 2))
        screen.blit(mensaje, rect)
        juego_activo = False

    pygame.display.flip()
    clock.tick(60)
