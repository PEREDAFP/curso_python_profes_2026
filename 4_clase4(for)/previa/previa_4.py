import pygame
import sys

#Vamos a crear dos plataformas y repetimos el tema de gravedad 
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
SUELO = pygame.Rect(0, 200 , 70 ,50)
SUELO1 = pygame.Rect(200, 300 , 70 ,50)

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
    rect1.y += GRAVEDAD
    # Visto esto preguntaremos a los alumnos por qué ocurrirá si vamos incrementando el número de plataformas
    # Plantearemos la posibilidad de trabajar con listas y, después de ver for, retomaremos con previa_5 
    if rect1.colliderect(SUELO): rect1.y = old_y
    if rect1.colliderect(SUELO1): rect1.y = old_y
    
    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, rect1)
    pygame.draw.rect(ventana, AZUL, SUELO)
    pygame.draw.rect(ventana, AZUL, SUELO1)
    pygame.display.flip()

    reloj.tick(FPS)
