import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dos rectángulos controlados por teclado")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Rectángulo 1 (rojo)
'''En el rectángulo:
rect.x: posición x en el lienzo, es la primera posición
rect.y: posición y en el lienzo, es la segunda posición
rect.w: anchura del rectángulo, es la tercera posición
rect.h: altura del rectángulo, es la cuarta posición

En el caso del rect1:
rect1.x = 100
rect1.y = 100
rect1.w = 50
rect1.h = 50

'''
rect1 = pygame.Rect(100, 100, 50, 50)

# Rectángulo 2 (azul)
rect2 = pygame.Rect(400, 200, 51, 52)
print(rect2.y, rect2.x, rect2.h, rect2.w)
# cambio
cambio = 5

# Reloj
reloj = pygame.time.Clock()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimiento del rectángulo rojo (jugador 1)
    if teclas[pygame.K_a]:
        rect1.x -= cambio
    if teclas[pygame.K_s]:
        rect1.x += cambio
    if teclas[pygame.K_w]:
        rect1.y -= cambio
    if teclas[pygame.K_z]:
        rect1.y += cambio

    # Movimiento del rectángulo azul (jugador 2)
    if teclas[pygame.K_k]:
        rect2.x -= cambio
    if teclas[pygame.K_o]:
        rect2.x += cambio
    if teclas[pygame.K_i]:
        rect2.y -= cambio
    if teclas[pygame.K_m]:
        rect2.y += cambio

    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, rect1)
    pygame.draw.rect(ventana, AZUL, rect2)
    pygame.display.flip()

    reloj.tick(60)
