import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 400, 300  #Otra forma, tipo tupla, de inicializar variables
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Texto")

# Fuente Arial
fuente = pygame.font.SysFont("Arial", 100)

# Variable en la que vamos a ir mostrando las pulsaciones
contador = 0

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Reloj
reloj = pygame.time.Clock()
FPS = 60


# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar en pantalla
    pantalla.fill(BLANCO)
    texto = fuente.render(str(contador), True, NEGRO)
    rect_texto = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
    pantalla.blit(texto, rect_texto)

    pygame.display.flip()
    reloj.tick(FPS)
