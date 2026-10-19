import sys
import pygame

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejemplo de Texto en Pygame")
reloj = pygame.time.Clock()

# 1. Definir fuentes
fuente_titulo = pygame.font.SysFont("Arial", 48, bold=True)
fuente_subtitulo = pygame.font.Font(None, 32)

# 2. Renderizar textos
superficie_titulo = fuente_titulo.render(
    "¡Hola, Pygame!", True, (255, 255, 255)
)
superficie_subtitulo = fuente_subtitulo.render(
    "Usa get_rect() para centrar elementos", True, (200, 200, 200)
)

# 3. Obtener rectángulos para posicionamiento
rect_titulo = superficie_titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 30))
rect_subtitulo = superficie_subtitulo.get_rect(
    center=(ANCHO // 2, ALTO // 2 + 30)
)


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pantalla.fill((30, 30, 30))

    # 4. Dibujar las superficies de texto
    pantalla.blit(superficie_titulo, rect_titulo)
    pantalla.blit(superficie_subtitulo, rect_subtitulo)

    pygame.display.flip()
    reloj.tick(60)

