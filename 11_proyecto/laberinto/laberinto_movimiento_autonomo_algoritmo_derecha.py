#Este código hace que el robot siempre deje a la derecha una pared
#Si no obstáculo a la derecha: giro a la derecha y avanzo
                        #En otro caso Si no obstáculo delante: avanzo
                        #En otro caso si no obstáculo izquierda: giro izquierda y avanzo
                        #En otro caso giro atrás y avanzo
#Observamos que también puede llevar a bucles sin fin si se producen cuadrados en los
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Constantes
TAMANIO_CUADRO = 40
FPS = 60
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Direcciones: (dy, dx) - derecha, abajo, izquierda, arriba
DIRECCIONES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#NOMBRES_DIRECCIONES = ['derecha', 'abajo', 'izquierda', 'arriba']
#Estas imágenes deben ser de TAMANIO_CUADROxTAMANIO_CUADRO píxeles
IMAGEN_DIRECCION = [ pygame.image.load('derecha.png'),
                    pygame.image.load('abajo.png'),
                    pygame.image.load('izquierda.png'),
                    pygame.image.load('arriba.png')]

# Leer el laberinto desde el archivo
def leer_laberinto(archivo):
    with open(archivo, 'r') as f:
        return [list(linea.rstrip('\n')) for linea in f.readlines()]

# Crear lista de obstáculos (rectángulos)
def crear_obstaculos(laberinto):
    obstaculos = []
    for y, fila in enumerate(laberinto):
        for x, celda in enumerate(fila):
            if celda == 'X':
                rect = pygame.Rect(x * TAMANIO_CUADRO, y * TAMANIO_CUADRO, TAMANIO_CUADRO, TAMANIO_CUADRO)
                obstaculos.append(rect)
    return obstaculos
def comprobar_libre(rect, obstaculos, direccion):
    nuevay = DIRECCIONES[direccion % 4][0]*TAMANIO_CUADRO
    nuevax = DIRECCIONES[direccion % 4][1]*TAMANIO_CUADRO
    nuevo_rect = rect.move(nuevax, nuevay)
    for obstaculo in obstaculos:
        if nuevo_rect.colliderect(obstaculo):
            return False
    return True

# Función principal
def main():
    # Configuración inicial
    laberinto = leer_laberinto('laberinto.txt')
    ancho = len(laberinto[0]) * TAMANIO_CUADRO
    alto = len(laberinto) * TAMANIO_CUADRO

    # Fuente mensaje final
    fuente = pygame.font.SysFont("Arial", 30)
    
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Laberinto")
    clock = pygame.time.Clock()
    
    # Crear obstáculos
    obstaculos = crear_obstaculos(laberinto)
    
    # Posición inicial del jugador (en píxeles)
    # Buscamos la primera celda que no sea obstáculo
    jugador_rect = IMAGEN_DIRECCION[0].get_rect()
    nuevo_rect = IMAGEN_DIRECCION[0].get_rect()
    encontrado = False
    for y in range(len(laberinto)):
        for x in range(len(laberinto[0])):
            if laberinto[y][x] != 'X':
                jugador_rect.x = x * TAMANIO_CUADRO
                jugador_rect.y = y * TAMANIO_CUADRO
                encontrado = True
                break
        if encontrado:
            break
    
    movimientos = 0
    juego_activo = True
    colision = 0
    direccion = 0

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if juego_activo:
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_SPACE:       
                        if comprobar_libre(jugador_rect,obstaculos,direccion + 1): direccion =(direccion+1)%4                 
                        elif comprobar_libre(jugador_rect,obstaculos,direccion): direccion =(direccion)%4
                        elif comprobar_libre(jugador_rect,obstaculos,direccion+2): direccion =(direccion+2)%4
                        elif comprobar_libre(jugador_rect,obstaculos,direccion+3):  direccion =(direccion+3)%4
                        
                        #Cambiamos la direccón del jugador y aumentamos los movimientos
                        jugador_rect.y += DIRECCIONES[direccion][0]*TAMANIO_CUADRO
                        jugador_rect.x += DIRECCIONES[direccion][1]*TAMANIO_CUADRO
                        movimientos += 1
                        
                        
                        # Verificar límites de la pantalla. Si el robot sale de la pantalla es porque ha llegado al final
                        if (jugador_rect.x < 0 or jugador_rect.x >= ancho or
                            jugador_rect.y < 0 or jugador_rect.y >= alto):
                            juego_activo = False
            
        # Dibujar
        
        if juego_activo:
            pantalla.fill(BLANCO)
            # Dibujar obstáculos
            for obstaculo in obstaculos:
                pygame.draw.rect(pantalla, NEGRO, obstaculo)
            # Dibujar jugador
            
            pantalla.blit(IMAGEN_DIRECCION[direccion], jugador_rect)
        else:
            #El juego ha terminado y se indican los movimientos y colisiones
            pantalla.fill(NEGRO)
            texto = fuente.render(f"Finalizado con {movimientos} movimientos y {colision} colisiones", True, BLANCO)
            rect_texto = texto.get_rect(center=(ancho // 2, alto // 2))
            pygame.draw.rect(pantalla, NEGRO, rect_texto)                    
            pantalla.blit(texto, rect_texto)
            
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()