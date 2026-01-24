"""
JUEGO CONVERSACIONAL CON DEEPSEEK API
DeepSeek + Pygame - Versión gratuita
-------------------------------------
"""

import pygame
import sys
from groq import Groq


# ------------------ CONFIGURACIÓN ------------------
pygame.init()
ANCHO, ALTO = 1200, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Conversacional con IA")
clock = pygame.time.Clock()
FPS = 60
Y_INICIAL = 70
Y_AUMENTO = 30
FONT = pygame.font.SysFont("arial", 22)

#Configuración Groq
#cliente = Groq(api_key="")
#hay que poner la API desde GROQ



# Personalidad del NPC
SYSTEM_PROMPT = """Eres el gran matemático Gödel. 
Responde de forma concisa (máximo 2-3 frases), manteniendo siempre el rol.
Explicarás  las preguntas que se te hagan para ser entendidas por un alumno de 4 de la ESO"""

mensajes_ia = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# ------------------ COLORES ------------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS =  (40, 40, 40)
AZUL = (100, 149, 237)
MOSTAZA = (200, 200, 100)

# ------------------ TEXTO ------------------
historial = [
    "NPC: ¡Hola alumno! Soy el lógico-matemático Gödel. ¿Alguna duda sobre completitud?"
]
entrada_usuario = ""




def responder_ia(texto_usuario):
    
    try:
        messages = [
            {"role": "system", "content": "Eres Gödel, el gran lógico. Responde en 1-2 frases."},
            {"role": "user", "content": texto_usuario}
        ]
        
        respuesta = cliente.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            temperature=1,
            #max_tokens=80,
            max_completion_tokens=8192,
            top_p=1,
            reasoning_effort="medium"
        )
        
        return "NPC: " + respuesta.choices[0].message.content
        
    except Exception as e:
        print(f"Error: {e}")
        return "NPC: (medito en silencio...)"





def dibujar_texto():
    # Fondo
    ventana.fill(GRIS)
    
    # Título
    titulo = pygame.font.SysFont("arial", 32, bold=True).render(
        "Aventura Conversacional", True, AZUL
    )
    ventana.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 10))
    
    # Historial de conversación
    y = Y_INICIAL
    for linea in historial[-8:]:  # Mostrar últimas 8 líneas
        color = BLANCO if linea.startswith("NPC:") else MOSTAZA
        texto = FONT.render(linea, True, color)
        ventana.blit(texto, (20, y))
        y += Y_AUMENTO

    # Caja de entrada
    pygame.draw.rect(ventana, NEGRO, (20, ALTO - 70, ANCHO - 40, 50), 0, 5)
    pygame.draw.rect(ventana, AZUL, (20, ALTO - 70, ANCHO - 40, 50), 2, 5)
    
    texto_entrada = FONT.render("> " + entrada_usuario + "|", True, BLANCO)
    ventana.blit(texto_entrada, (30, ALTO - 55))
    
    # Instrucciones
    instrucciones = FONT.render("Presiona ENTER para enviar, ESC para salir", True, (150, 150, 150))
    ventana.blit(instrucciones, (ANCHO//2 - instrucciones.get_width()//2, ALTO - 120))

# ------------------ BUCLE PRINCIPAL ------------------
ejecutando = True
while ejecutando:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ejecutando = False
                
            elif event.key == pygame.K_RETURN:
                if entrada_usuario.strip() != "":
                    historial.append("Tú: " + entrada_usuario)
                    respuesta = responder_ia(entrada_usuario)
                    print(respuesta)
                    historial.append(respuesta)
                    entrada_usuario = ""
                    
            elif event.key == pygame.K_BACKSPACE:
                entrada_usuario = entrada_usuario[:-1]
            elif event.key == pygame.K_TAB:
                # Autocompletar saludo
                entrada_usuario = "Hola, ¿quién eres?"
            else:
                entrada_usuario += event.unicode

    dibujar_texto()
    pygame.display.flip()

pygame.quit()
sys.exit()