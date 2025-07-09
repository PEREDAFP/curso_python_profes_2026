import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Cuadro rojo sobre fondo blanco")

# Definir colores


# Bucle principal

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas presionadas

    # Dibujar escena
    ventana.fill((255,255,255))
    pygame.draw.rect(ventana, (255,0,0), (50,50,50,50))
    pygame.display.flip()
