import pygame, sys
 

#VARIABLES Y CONSTANTES
#anchos y altos de ventana y personaje

ANCHO_VENTANA = 400
ALTO_VENTANA = 300 

ANCHO_IMAGEN = 100
TOTAL_MOVIMIENTOS = 9
MARGEN_SUPERIOR = 0
ANCHO_PERSONAJE = 90
ALTO_PERSONAJE = 175

#Para el cálculo de la posición
pos_x = 0
pos_y = ALTO_VENTANA - ALTO_PERSONAJE

AUMENTO_PIXELES_X = 2
#Para obtener desde dónde cortar la imagen
margen = 0



 
pygame.init()
 

visor = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) 
pygame.display.set_caption("Movimiento personaje sin lista")
pygame.key.set_repeat(1,25)
bicho = pygame.image.load('hombreAndando.png')

# Reloj
reloj = pygame.time.Clock()
FPS = 60 

#Colores

BLANCO = (255,255,255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        teclasPulsadas = pygame.key.get_pressed()
        if teclasPulsadas[pygame.K_a]:
            pos_x -=  AUMENTO_PIXELES_X
            margen -= ANCHO_IMAGEN
            margen %= (ANCHO_IMAGEN * TOTAL_MOVIMIENTOS)
            
        if teclasPulsadas[pygame.K_s]:
            pos_x += AUMENTO_PIXELES_X
            margen += ANCHO_IMAGEN
            margen %= (ANCHO_IMAGEN * TOTAL_MOVIMIENTOS)
        
        visor.fill(BLANCO)
        visor.blit(bicho, (pos_x, pos_y), (margen,MARGEN_SUPERIOR,ANCHO_PERSONAJE, ALTO_PERSONAJE))
        pygame.display.flip()
        reloj.tick(FPS)
    