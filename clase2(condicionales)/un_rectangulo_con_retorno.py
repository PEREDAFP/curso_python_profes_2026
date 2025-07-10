import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Un rectángulo con retorno")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

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


# cambio
cambio = 1

# Reloj
reloj = pygame.time.Clock()
FPS = 150

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimiento del rectángulo rojo (jugador 1)
    if teclas[pygame.K_a]:
        #Cuando todo el rectángulo haya salido por la izquierda volverá por la derecha
        if rect1.x + rect1.w <0:
            rect1.x = ANCHO
        else:
            rect1.x -= cambio 

    if teclas[pygame.K_s]:
        #Cuando todo el rectángulo haya salido por la derecha volverá por la izquierda
        if rect1.x > ANCHO:
            rect1.x = -rect1.w
        else:
            rect1.x += cambio

    if teclas[pygame.K_w]:
        #Cuando todo el rectángulo haya salido por arriba volverá por abajo
        if rect1.y + rect1.h < 0:
            rect1.y = ALTO
        else:    
            rect1.y -= cambio
    if teclas[pygame.K_z]:
        #Cuando todo el rectángulo haya salido pro abajo volverá por arri ba
        if rect1.y > ALTO:
            rect1.y = -rect1.h
        else:
            rect1.y += cambio

   
    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, rect1)
    pygame.display.flip()

    reloj.tick(FPS)
