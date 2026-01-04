import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento con las teclas de flecha")

# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Rectángulo
rect_x = 100
rect_y = 100
rect_ancho = 50
rect_alto = 50
cambio = 5

# Bucle principal
reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas presionadas

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        rect_x -= cambio
    if teclas[pygame.K_RIGHT]:
        rect_x += cambio
    if teclas[pygame.K_UP]:
        rect_y -= cambio
    if teclas[pygame.K_DOWN]:
        rect_y += cambio

    # Dibujar escena
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, (rect_x, rect_y, rect_ancho, rect_alto))
    pygame.display.flip()

    # Limitar a 60 FPS
    # Cambia este 60 por otros valores diferentes: 20, 50, 100
    reloj.tick(60)
