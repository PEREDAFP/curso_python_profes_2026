import pygame
import sys

# Inicializar Pygame
pygame.init()

# Tamaño de pantalla
ANCHO, ALTO = 800, 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rectángulo que dispara")

# Reloj para controlar FPS
clock = pygame.time.Clock()
FPS = 60

# Rectángulo del jugador
jugador = pygame.Rect(400, 500, 50, 50)
color_jugador = (0, 200, 255)
velocidad = 5

# Lista de disparos
disparos = []
color_disparo = (255, 255, 0)
vel_disparo = 7

# Bucle principal
while True:
    # --- Capturar eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Disparar al pulsar ESPACIO
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

    # --- Actualizar disparos ---
    for d in disparos:
        d.y -= vel_disparo  # mover hacia arriba

    # Eliminar disparos que salen de la pantalla
    for d in disparos:
        if d.top < 10:
            disparos.remove(d)
            
    #Una forma más elegante con comprehension list
    #disparos = [d for d in disparos if d.bottom > 0]

    # --- Dibujar todo ---
    screen.fill((30, 30, 30))  # fondo
    pygame.draw.rect(screen, color_jugador, jugador)  # jugador

    for d in disparos:
        pygame.draw.rect(screen, color_disparo, d)  # disparos

    pygame.display.flip()
    clock.tick(FPS)
