import pygame
#Se debe utilizar
def dibuja_mensaje(texto, fuente, tamanio_fuente, color, posicion):
    fuente_interna = pygame.font.SysFont(fuente, tamanio_fuente)
    texto = fuente_interna.render(texto, True, color)
    rect = texto.get_rect()
    rect.x, rect.y = posicion
    return (texto, rect)