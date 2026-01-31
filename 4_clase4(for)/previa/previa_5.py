import pygame
import sys
import random

# ¿Y si añadimos más plataformas? ¿3? ¿10?....
# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Vamos a crear varias plataformas")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0,0,255)

# Rectángulo 1 (rojo)
rect1 = pygame.Rect(100, 100, 50, 50)

# Plataformas
ALTO_PLATAFORMA = 50
ANCHO_PLATAFORMA = 150
SUELO = []
for i in range(4):
    SUELO.append(pygame.Rect(i* ANCHO_PLATAFORMA + 50, ALTO - i * ALTO_PLATAFORMA - ALTO_PLATAFORMA, random.randint(50,ANCHO_PLATAFORMA),ALTO_PLATAFORMA))


# cambio de x según pulsación
cambio = 5

# Gravedad
GRAVEDAD = 3

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
    # Vamos a copiar las coordenadas por si ha habido un choque retomar al anterior sitio
    old_x, old_y = rect1.x, rect1.y
    # Movimiento del rectángulo rojo 
    if teclas[pygame.K_LEFT]:
        #Cambiaremos rect1.x si rect1.x previo es mayor que cero
        if rect1.x > 0: rect1.x -= cambio
    if teclas[pygame.K_RIGHT]:
        #Cambiaremos rect1.x más su ancho es menor que ANCHO
        if ( rect1.x + rect1.w ) < ANCHO: rect1.x += cambio
    if teclas[pygame.K_UP]:
        #Cambiaremos rect1.y si su valor es mayor que 0
        if rect1.y > 0: rect1.y -= cambio
    if teclas[pygame.K_DOWN]:
        #Cambiaremos rect1.y si su valor más la altura es menor que ALTO
        if ( rect1.y + rect1.h ) < ALTO: rect1.y += cambio
    rect1.y += GRAVEDAD
    for i in SUELO:
        if rect1.colliderect(i):
            rect1.y = old_y
            break
    
    
    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, rect1)
    for i in SUELO:
        pygame.draw.rect(ventana, AZUL, i)
    
    pygame.display.flip()

    reloj.tick(FPS)
