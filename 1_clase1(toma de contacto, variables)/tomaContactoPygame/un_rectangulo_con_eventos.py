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
FPS = 60
reloj = pygame.time.Clock()
#Al cambiar la captura con eventos observaremos que la fluidez del juego es mucho peor.
# Deben utilizarse los eventos únicamente para cosas muy esporádicas: Cerrar ventanas, disparos del personaje, etc.
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            # Teclas presionadas
            match evento.key:
                case pygame.K_LEFT:
                    rect_x -= cambio
                case pygame.K_RIGHT:
                     rect_x += cambio
                case pygame.K_UP:
                    rect_y -= cambio
                case pygame.K_DOWN:
                    rect_y += cambio
    # Dibujar escena
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, (rect_x, rect_y, rect_ancho, rect_alto))
    pygame.display.flip()

    # Limitar a 60 FPS
    reloj.tick(FPS)
