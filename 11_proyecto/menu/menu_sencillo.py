import pygame
import sys

# Inicialización
pygame.init()
ANCHO, ALTO = 800, 600
ANCHO_BOTON, ALTO_BOTON = 250, 50
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menú simple")
clock = pygame.time.Clock()
FPS = 60

# Fuente
FUENTE = pygame.font.SysFont(None, 60)


# Opciones del menú
opciones = ["OPCIÓN 1", "OPCIÓN 2", "OPCIÓN 3", "OPCIÓN4 "]
seleccion = 0
MARGEN = (ANCHO // 2 ) - ( ANCHO_BOTON // 2)
#Para el espaciado de las opciones

ESPACIADO_OPCIONES = 80
total_altura = ESPACIADO_OPCIONES * (len(opciones)-1)
INICIO_Y = 100+ (ALTO // 2 ) - ( total_altura // 2)

# Función para mostrar una pantalla negra con el nombre de la opción
def mostrar_opcion(nombre):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return  # volver al menú principal

        pantalla.fill((0, 0, 0))
        texto = FUENTE.render(nombre, True, (255, 255, 255))
        rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(texto, rect)
        pygame.display.flip()
        clock.tick(60)

# Bucle principal del menú
while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                seleccion = (seleccion + 1) % len(opciones)
            elif event.key == pygame.K_UP:
                seleccion = (seleccion - 1) % len(opciones)
            elif event.key == pygame.K_RETURN:
                mostrar_opcion(opciones[seleccion])
        #Si pulsamos el ratón con el botón izquierdo        
        #Pruebe el alumno a cambiar event.button por 2 y 3
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(rects):
                #Si al hacer un recorrido por los rectángulos, alguno coincide con el 
                #puntero del ratón cuando se ha pulsado el botón correspondiente
                if rect.collidepoint(mouse_pos):
                    seleccion = i
                    mostrar_opcion(opciones[i])

    # Dibujar menú
    pantalla.fill((30, 30, 40))
    titulo = FUENTE.render("MENÚ PRINCIPAL", True, (255, 255, 255))
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 80))

    rects = []
    for i, texto in enumerate(opciones):
        if i == seleccion:
            color = (180,180,180)
        else:
            color = (70, 130, 200) 
            #Más pythonico color = (70,130,200) if i == seleccion else (180, 180, 180)
        texto = FUENTE.render(texto, True, color)
        
        rect = texto.get_rect(center=(ANCHO // 2, INICIO_Y + i * ESPACIADO_OPCIONES))
        rect.x = MARGEN
        rect.size=(ANCHO_BOTON, ALTO_BOTON)
        pygame.draw.rect(pantalla, (255,255,255), rect, border_radius=8)
        rects.append(rect)
        pantalla.blit(texto, rect)

        # Detectar hover con ratón
        if rect.collidepoint(mouse_pos):
            seleccion = i

    pygame.display.flip()
    clock.tick(FPS)
