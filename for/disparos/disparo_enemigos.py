import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Tamaño de pantalla
ANCHO, ALTO = 800, 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rectángulo que dispara y destruye enemigos")

# Reloj para controlar FPS
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

# Crear enemigos iniciales
for i in range(5):
    x = random.randint(50, ANCHO - 50)
    y = random.randint(50, 200)
    enemigo = pygame.Rect(x, y, 50, 50)
    enemigos.append(enemigo)

# --- Bucle principal ---
while True:
    # --- Capturar eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Disparar con espacio
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Crear un nuevo disparo en el centro superior del jugador
                nuevo_disparo = pygame.Rect(jugador.centerx - 5, jugador.top - 10, 10, 20)
                disparos.append(nuevo_disparo)

    # --- Movimiento del jugador ---
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= velocidad
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += velocidad

    # --- Movimiento de los enemigos ---
    for e in enemigos:
        e.y += vel_enemigo
        # Si bajan del todo, los reposicionamos arriba (vuelven a aparecer)
        if e.top > ALTO:
            e.y = random.randint(-100, -40)
            e.x = random.randint(50, ANCHO - 50)

    # --- Movimiento de disparos ---
    for d in disparos:
        d.y -= vel_disparo

    # Eliminar disparos que salen de la pantalla
    disparos = [d for d in disparos if d.bottom > 0]

    # --- Detectar colisiones entre disparos y enemigos ---
    for d in disparos[:]:
        for e in enemigos[:]:
            if d.colliderect(e):
                disparos.remove(d)
                enemigos.remove(e)
                break  # salir del bucle de enemigos

    # --- Dibujar todo ---
    screen.fill((30, 30, 30))  # fondo

    # Jugador
    pygame.draw.rect(screen, color_jugador, jugador)

    # Disparos
    for d in disparos:
        pygame.draw.rect(screen, color_disparo, d)

    # Enemigos
    for e in enemigos:
        pygame.draw.rect(screen, color_enemigo, e)

    # Si no quedan enemigos, mostrar mensaje
    if not enemigos:
        fuente = pygame.font.SysFont(None, 60)
        texto = fuente.render("¡Has ganado!", True, (255, 255, 255))
        rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
        screen.blit(texto, rect)

    pygame.display.flip()
    clock.tick(60)
