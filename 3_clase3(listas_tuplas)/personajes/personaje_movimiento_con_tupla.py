import pygame, sys
'''
Para trabajar con este script basta con cambiar en bicho la imagen que queremos cargar
He dejado los movbicho con las coordenadas que representan cada movimento de hombreAndando y Ken1
Basta con descomentar y comentar los movbicho correspondientes
'''

 
pygame.init()

ANCHO = 400
ALTO = 400
visor = pygame.display.set_mode((ANCHO,ALTO))
 
pygame.display.set_caption("Movimientos Personaje desde lista")
 
#bicho = pygame.image.load('Ken1.png')
bicho = pygame.image.load('hombreAndando.png')

#Colores
BLANCO = (255, 255, 255)

#Reloj
reloj = pygame.time.Clock()
FPS = 60 

#Variables para el control del movimiento 
fase_mov = 0 #zona de la imagen a representar en la ventana
pos = 50 #posición x de la ventana donde se mostrará al personaje


#Las listas con las coordenadas de movimiento de los diferentes personajes
#[(margenizquierdo, posicion_más_alta, ancho, alto )]
 
#movbicho=[(0,0,150,50), (50,0,50,50),(100,0,50,50),(150,0,50,50)] 
#movbicho esquemático
#movbicho=[(0,0,200,400),(400,0,200,400),(600,0,200,400),(1000,0,200,400)]
#movbicho hombre andando
movbicho = ((0,0,90,175),(100,0,90,175),(200,0,90,175),(300,0,90,175),
            (400,0,90,175),(500,0,90,175),(600,0,90,175),(700,0,90,175),
            (800,0,90,175))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclasPulsadas = pygame.key.get_pressed()
    if teclasPulsadas[pygame.K_a]:
        pos -= 10
        fase_mov -= 1
        if fase_mov <0: 
            fase_mov = len(movbicho) - 1
    
    if teclasPulsadas[pygame.K_s]:
        pos += 10
        fase_mov += 1
        if fase_mov >= len(movbicho):
            fase_mov = 0
    
    visor.fill(BLANCO)
    visor.blit(bicho, (pos,100), movbicho[fase_mov])
    pygame.display.flip()
    reloj.tick(FPS)
    