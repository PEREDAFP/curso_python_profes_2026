#Algorimo mano derecha:
# Siempre antes de moverse:
#    - Comprueba la celda de su derecha
#    - Si está libre: gira a la derecha y avanza
#    - Si no:
#        - Mirar al frente y si está libre: avanzar
#        - Si tampoco: girar a la izquierda sin avanzar y contamos una colisión

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

def girar_derecha(d): return (d + 1) % 4
def girar_izquierda(d): return (d - 1) % 4


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

def puede_moverse(rect, direccion, obstaculos):
    dx = DIRECCIONES[direccion][1] * TAMANIO_CUADRO
    dy = DIRECCIONES[direccion][0] * TAMANIO_CUADRO

    rect_prueba = rect.copy()
    rect_prueba.x += dx
    rect_prueba.y += dy

    for obstaculo in obstaculos:
        if rect_prueba.colliderect(obstaculo):
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
                       # comprobar derecha
                        dir_derecha = girar_derecha(direccion)
                        if puede_moverse(jugador_rect, dir_derecha, obstaculos):
                            direccion = dir_derecha


                        # comprobar frente
                        if puede_moverse(jugador_rect, direccion, obstaculos):
                            jugador_rect.y += DIRECCIONES[direccion][0] * TAMANIO_CUADRO
                            jugador_rect.x += DIRECCIONES[direccion][1] * TAMANIO_CUADRO
                            movimientos += 1
                        else:
                            # girar izquierda si no puede avanzar. Ya avanzará en la siguiente vuelta.
                            direccion = girar_izquierda(direccion)
                            colision += 1
                        
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