import pygame, sys
 
 
pygame.init()
 

visor = pygame.display.set_mode((400,800))
 
pygame.display.set_caption("Movimientos Personaje desde lista")
 
#bicho = pygame.image.load('Ken1.png')
bicho = pygame.image.load('hombreAndando.png')
pygame.key.set_repeat(1,25)
# Reloj
reloj = pygame.time.Clock()
 
 
fasemov=0
 
pos=50
 
#[(margenizquierdo, posicion_más_alta, ancho, alto )]
 
#movbicho=[(0,0,150,50), (50,0,50,50),(100,0,50,50),(150,0,50,50)] 
#movbicho esquemático
#movbicho=[(0,0,200,400),(400,0,200,400),(600,0,200,400),(1000,0,200,400)]
#movbicho hombre andando
movbicho = [(0,0,90,175),(100,0,90,175),(200,0,90,175),(300,0,90,175),(400,0,90,175),(500,0,90,175),(600,0,90,175),(700,0,90,175),(800,0,90,175)] 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        teclasPulsadas = pygame.key.get_pressed()
        if teclasPulsadas[pygame.K_a]:
            pos-=1
            fasemov -= 1
            if fasemov <0: 
               fasemov = len(movbicho) - 1
        
        if teclasPulsadas[pygame.K_s]:
            pos+=1
            fasemov += 1
            if fasemov >= len(movbicho):
                fasemov = 0
        
        visor.fill((255,255,255))
        visor.blit(bicho, (pos,100), movbicho[fasemov])
        pygame.display.flip()
        reloj.tick(40)
    