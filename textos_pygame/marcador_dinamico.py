import sys
import pygame
from soupsieve import match

pygame.init()
ANCHO,ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 1: Contador")
reloj = pygame.time.Clock()

COLOR_FUENTE = (255, 215, 0)
COLOR_FONDO = (20, 20, 20)
POSICION_TEXTO = (50, 50)

fuente = pygame.font.SysFont("Arial", 40)
puntuacion = 0

FPS=60


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif  evento.type == pygame.KEYDOWN:
            match evento.key:
                case  pygame.K_UP:
                    puntuacion += 10
                case pygame.K_DOWN:
                    puntuacion -= 10

    pantalla.fill(COLOR_FONDO)

    # Renderizado dinámico dentro del bucle principal
    texto_puntos = fuente.render(
        f"Puntos: {puntuacion}", True, COLOR_FUENTE
    )
    pantalla.blit(texto_puntos, POSICION_TEXTO)

    pygame.display.flip()
    reloj.tick(FPS)

