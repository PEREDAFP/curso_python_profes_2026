import pygame, sys
 
'''
Repetimos el ejercicio que ya hicimos con el rectángulo para que el personaje tenga un movimiento continuo a 
través de la pantalla.
Esto nos va a permitir trabajar con diferentes escenarios como veremos en el siguiente ejercicio.
'''
# Colores
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
NEGRO = (0,0,0)
BLANCO = (255,255,255)


#VARIABLES Y CONSTANTES
#anchos y altos de ventana y personaje



ANCHO_VENTANA = 500
ALTO_VENTANA = 300 

ANCHO_IMAGEN = 100
TOTAL_MOVIMIENTOS = 9
MARGEN_SUPERIOR = 0
ANCHO_PERSONAJE = 90
ALTO_PERSONAJE = 175

#Para el cálculo de la posición
pos_x = 0
pos_y = ALTO_VENTANA - ALTO_PERSONAJE

AUMENTO_PIXELES_X = 10
#Para obtener desde dónde cortar la imagen
margen = 0

# Escenarios: vamos a utilizar una lista con colores, pero podría crearse con imágenes, con otros elementos que permitieran 
# mostrar profundidad o túneles, escaleras, etc.

ESCENARIOS = (ROJO, VERDE, AZUL, NEGRO, BLANCO)
cont_escenario = 0
 
pygame.init()
 

visor = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) 
pygame.display.set_caption("Movimiento personaje sin lista en distintos escenarios")
pygame.key.set_repeat(1,25)
bicho = pygame.image.load('hombreAndando.png')

# Reloj
reloj = pygame.time.Clock()
FPS = 60 

#Colores




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
        #Hacemos que el movimiento del personaje sea cíclico en la pantalla
        #Si sale por la derecha, vuelve por la izquierda. Dejamos al alumno que cambie -ANCHO_IMAGEN por 0 
        if pos_x > ANCHO_VENTANA: 
            pos_x = -ANCHO_IMAGEN
            cont_escenario += 1
            cont_escenario %= len(ESCENARIOS)
        #Si sale por la izquierda, vuelve poºr la derecha
        if (pos_x + ANCHO_IMAGEN) < 0: 
            pos_x = ANCHO_VENTANA
            cont_escenario -= 1
            cont_escenario %= len(ESCENARIOS)

        
        #Después de los cálculos dibujamos todo
        visor.fill(ESCENARIOS[cont_escenario])
        visor.blit(bicho, (pos_x, pos_y), (margen,MARGEN_SUPERIOR,ANCHO_PERSONAJE, ALTO_PERSONAJE))
        pygame.display.flip()
        reloj.tick(FPS)
    