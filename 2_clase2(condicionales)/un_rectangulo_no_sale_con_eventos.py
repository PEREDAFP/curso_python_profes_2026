import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Un rectángulo que no sale de la ventana")
pygame.key.set_repeat(1,10)
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
# Aquí vamos a utilizar eventos, por lo que nos interesa trabajar con pygame.key.set_repeat(1,10)
# Recuerda que el segundo parámetro cuanto más bajo, más FPS.
# Ten en cuenta que trabajar con eventos para el movimiento de un "personaje" es una  mala opción
# en este caso lo estamos haciendo simplemente como ejercicio.
# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            # match ha sido introducido a partir de python 3.10. No funcionará en versiones anteriores
            match evento.key:
                case pygame.K_a:
                    #Cambiaremos rect1.x si rect1.x previo es mayor que cero
                    if rect1.x > 0: rect1.x -= cambio
                case pygame.K_s:
                    #Cambiaremos rect1.x más su ancho es menor que ANCHO
                    if ( rect1.x + rect1.w ) < ANCHO: rect1.x += cambio
                case pygame.K_w:
                    #Cambiaremos rect1.y si su valor es mayor que 0
                    if rect1.y > 0: rect1.y -= cambio
                case pygame.K_z:
                    #Cambiaremos rect1.y si su valor más la altura es menor que ALTO
                    if ( rect1.y + rect1.h ) < ALTO: rect1.y += cambio
        # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, rect1)
    pygame.display.flip()

    #reloj.tick(FPS)
