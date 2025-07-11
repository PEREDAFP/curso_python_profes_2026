import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 400, 300
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Contador con Teclado y con evento")

# Fuente Arial
fuente = pygame.font.SysFont("Arial", 100)
contador = 0

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Bucle principal
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_PLUS or evento.key == pygame.K_KP_PLUS:
                contador += 1
            elif evento.key == pygame.K_MINUS or evento.key == pygame.K_KP_MINUS:
                contador -= 1

    # Dibujar en pantalla
    pantalla.fill(BLANCO)
    texto = fuente.render(str(contador), True, NEGRO)
    rect_texto = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
    pantalla.blit(texto, rect_texto)

    pygame.display.flip()
    reloj.tick(30)
