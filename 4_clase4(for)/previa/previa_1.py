import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Vamos a crear varios rectángulos")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Rectángulo 1 (rojo)

rect1 = pygame.Rect(100, 100, 50, 50)


# cambio de x según pulsación
cambio = 5

# Reloj
reloj = pygame.time.Clock()
FPS = 60

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimiento del rectángulo rojo 
    if teclas[pygame.K_a]:
        #Cambiaremos rect1.x si rect1.x previo es mayor que cero
        if rect1.x > 0: rect1.x -= cambio
    if teclas[pygame.K_s]:
        #Cambiaremos rect1.x más su ancho es menor que ANCHO
        if ( rect1.x + rect1.w ) < ANCHO: rect1.x += cambio
    if teclas[pygame.K_w]:
        #Cambiaremos rect1.y si su valor es mayor que 0
        if rect1.y > 0: rect1.y -= cambio
    if teclas[pygame.K_z]:
        #Cambiaremos rect1.y si su valor más la altura es menor que ALTO
        if ( rect1.y + rect1.h ) < ALTO: rect1.y += cambio

    print(f"El centro del rectángulo {rect1.center}")
    print(f"El centro x del rectángulo {rect1.centerx}")
    print(f"El centro y del rectángulo {rect1.centery}")
    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, rect1)
    pygame.display.flip()

    reloj.tick(FPS)
