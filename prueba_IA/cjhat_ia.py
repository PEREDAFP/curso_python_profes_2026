"""
BOCETO DE JUEGO CONVERSACIONAL
Modelo LLM + Pygame (estructura base)
--------------------------------
Este ejemplo muestra la arquitectura general.
NO incluye una clave real de API.
"""

import pygame
import sys

# ------------------ CONFIGURACIÓN ------------------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego Conversacional")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 22)

# ------------------ COLORES ------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)

# ------------------ TEXTO ------------------
historial = [
    "NPC: Hola viajero. ¿Qué deseas hacer?"
]
entrada_usuario = ""

# ------------------ IA (SIMULADA) ------------------
def responder_ia(texto_usuario):
    """
    Aquí iría la llamada real a nuestro LLM.
    De momento devolvemos respuestas simuladas.
    """
    texto_usuario = texto_usuario.lower()

    if "hola" in texto_usuario:
        return "NPC: Saludos, aventurero."
    elif "ayuda" in texto_usuario:
        return "NPC: Puedes explorar, preguntar o marcharte."
    elif "adios" in texto_usuario:
        return "NPC: Que los vientos te acompañen."
    else:
        return "NPC: No comprendo tu petición."

# ------------------ DIBUJADO ------------------
def dibujar_texto():
    screen.fill(GRAY)

    y = 20
    for linea in historial[-10:]:  # Mostrar últimas líneas
        texto = FONT.render(linea, True, WHITE)
        screen.blit(texto, (20, y))
        y += 28

    # Caja de entrada
    pygame.draw.rect(screen, BLACK, (20, HEIGHT - 60, WIDTH - 40, 40))
    texto_input = FONT.render(entrada_usuario, True, WHITE)
    screen.blit(texto_input, (30, HEIGHT - 52))

# ------------------ BUCLE PRINCIPAL ------------------
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if entrada_usuario.strip() != "":
                    historial.append("Tú: " + entrada_usuario)
                    respuesta = responder_ia(entrada_usuario)
                    historial.append(respuesta)
                    entrada_usuario = ""

            elif event.key == pygame.K_BACKSPACE:
                entrada_usuario = entrada_usuario[:-1]
            else:
                entrada_usuario += event.unicode

    dibujar_texto()
    pygame.display.flip()

pygame.quit()
sys.exit()
