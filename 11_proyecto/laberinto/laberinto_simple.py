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

# Leer el laberinto desde el archivo
def leer_laberinto(archivo):
    with open(archivo, 'r') as f:
        return [list(linea.strip()) for linea in f.readlines()]

# Crear lista de obstáculos (rectángulos)
def crear_obstaculos(laberinto):
    obstaculos = []
    for y, fila in enumerate(laberinto):
        for x, celda in enumerate(fila):
            if celda == 'X':
                rect = pygame.Rect(x * TAMANIO_CUADRO, y * TAMANIO_CUADRO, TAMANIO_CUADRO, TAMANIO_CUADRO)
                obstaculos.append(rect)
    return obstaculos

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
    # Buscamos la primera celda que no sea obstáculo para poner a nuestro robot
    jugador_rect = pygame.Rect(0, 0, TAMANIO_CUADRO, TAMANIO_CUADRO)
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
    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if juego_activo:
                if event.type == pygame.KEYDOWN:
                    # Guardar la posición actual por si hay que revertir
                    old_x, old_y = jugador_rect.x, jugador_rect.y
                    
                    if event.key == pygame.K_UP:
                        jugador_rect.y -= TAMANIO_CUADRO
                    elif event.key == pygame.K_DOWN:
                        jugador_rect.y += TAMANIO_CUADRO
                    elif event.key == pygame.K_LEFT:
                        jugador_rect.x -= TAMANIO_CUADRO
                    elif event.key == pygame.K_RIGHT:
                        jugador_rect.x += TAMANIO_CUADRO
                    print(jugador_rect.y)
                    print(jugador_rect.x)
                    movimientos += 1
                    
                    # Verificar colisiones con obstáculos
                    for obstaculo in obstaculos:
                        if jugador_rect.colliderect(obstaculo):
                            jugador_rect.x, jugador_rect.y = old_x, old_y
                            colision += 1
                            break
                    
                    # Verificar límites de la pantalla
                    if (jugador_rect.x < 0 or jugador_rect.x >= ancho or
                        jugador_rect.y < 0 or jugador_rect.y >= alto):
                        #Esto lo voy a cambiar por un juego_activo = False
                        juego_activo = False
        
        # Dibujar
        
        if juego_activo:
            pantalla.fill(BLANCO)
            # Dibujar obstáculos
            for obstaculo in obstaculos:
                pygame.draw.rect(pantalla, NEGRO, obstaculo)
            
            # Dibujar jugador
            pygame.draw.rect(pantalla, ROJO, jugador_rect)
        else:
            pantalla.fill(NEGRO)
            texto = fuente.render(f"Finalizado con {movimientos} movimientos y {colision} colisiones", True, BLANCO)
            rect_texto = texto.get_rect(center=(ancho // 2, alto // 2))
            #Para darle ancho y alto al botón
            #Si quisiéramos darle fondo al texto con un borde, muy útil para botones en un menú
            pygame.draw.rect(pantalla, NEGRO, rect_texto)                    
            pantalla.blit(texto, rect_texto)
            
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()