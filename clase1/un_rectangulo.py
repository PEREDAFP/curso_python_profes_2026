import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento con teclas A, S, W, Z")

# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Rectángulo
rect_x = 100
rect_y = 100
rect_ancho = 50
rect_alto = 50
velocidad = 5

# Bucle principal
reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        rect_x -= velocidad
    if teclas[pygame.K_s]:
        rect_x += velocidad
    if teclas[pygame.K_w]:
        rect_y -= velocidad
    if teclas[pygame.K_z]:
        rect_y += velocidad

    # Dibujar escena
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, (rect_x, rect_y, rect_ancho, rect_alto))
    pygame.display.flip()

    # Limitar a 60 FPS
    reloj.tick(60)
