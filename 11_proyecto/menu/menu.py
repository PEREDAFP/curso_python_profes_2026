import pygame
import json
import sys

# -------------------------------
# Cargar opciones desde JSON
# -------------------------------
with open("menu.json", "r", encoding="utf-8") as f:
    MENU_ITEMS = json.load(f)

# -------------------------------
# Inicialización pygame
# -------------------------------
pygame.init()
SCREEN_W, SCREEN_H = 800, 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Menú dinámico con scroll")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 40)
BIG_FONT = pygame.font.SysFont(None, 60)

# -------------------------------
# Pantalla de opción seleccionada
# -------------------------------
def mostrar_opcion(nombre):
    """Muestra una pantalla negra con el nombre de la opción."""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # volver al menú

        screen.fill((0, 0, 0))
        texto = BIG_FONT.render(nombre, True, (255, 255, 255))
        rect = texto.get_rect(center=(SCREEN_W//2, SCREEN_H//2))
        screen.blit(texto, rect)
        pygame.display.flip()
        clock.tick(60)

# -------------------------------
# Clase del menú con scroll
# -------------------------------
class Menu:
    def __init__(self, items):
        self.items = items
        self.selected = 0
        self.scroll_y = 0
        self.item_height = 70
        self.visible_height = SCREEN_H - 180  # margen superior e inferior
        self.max_scroll = max(0, len(items) * self.item_height - self.visible_height)

    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected = min(self.selected + 1, len(self.items) - 1)
                        self.ensure_visible()
                    elif event.key == pygame.K_UP:
                        self.selected = max(self.selected - 1, 0)
                        self.ensure_visible()
                    elif event.key == pygame.K_RETURN:
                        self.activar_opcion(self.selected)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # clic
                        for i, rect in enumerate(self.item_rects):
                            if rect.collidepoint(mouse_pos):
                                self.selected = i + self.first_visible_index
                                self.activar_opcion(self.selected)
                    elif event.button == 4:  # rueda arriba
                        self.scroll_y = max(self.scroll_y - 30, 0)
                    elif event.button == 5:  # rueda abajo
                        self.scroll_y = min(self.scroll_y + 30, self.max_scroll)

            # Calcular qué elementos son visibles
            self.first_visible_index = self.scroll_y // self.item_height
            self.last_visible_index = min(
                len(self.items),
                self.first_visible_index + int(self.visible_height // self.item_height) + 1
            )

            # Dibujar fondo
            screen.fill((30, 30, 40))
            titulo = BIG_FONT.render("Menú Principal", True, (255, 255, 255))
            screen.blit(titulo, (SCREEN_W//2 - titulo.get_width()//2, 40))

            # Dibujar opciones visibles
            self.item_rects = []
            base_y = 160 - (self.scroll_y % self.item_height)

            for visible_i, i in enumerate(range(self.first_visible_index, self.last_visible_index)):
                item = self.items[i]
                text = FONT.render(item["nombre"], True, (255, 255, 255))
                rect = pygame.Rect(0, 0, 300, 50)
                rect.center = (SCREEN_W // 2, base_y + visible_i * self.item_height)
                self.item_rects.append(rect)

                color = (70, 130, 200) if i == self.selected else (80, 80, 80)
                pygame.draw.rect(screen, color, rect, border_radius=8)
                screen.blit(text, (rect.x + 20, rect.y + 10))

            # Dibujar barra de scroll si hace falta
            if self.max_scroll > 0:
                bar_h = max(40, (self.visible_height / (len(self.items) * self.item_height)) * self.visible_height)
                bar_y = 160 + (self.scroll_y / self.max_scroll) * (self.visible_height - bar_h)
                pygame.draw.rect(screen, (120, 120, 120), (SCREEN_W - 30, bar_y, 10, bar_h), border_radius=4)

            pygame.display.flip()
            clock.tick(60)

    def ensure_visible(self):
        """Ajusta el scroll para mantener la opción seleccionada visible."""
        top_y = self.selected * self.item_height
        bottom_y = top_y + self.item_height
        if top_y < self.scroll_y:
            self.scroll_y = max(0, top_y)
        elif bottom_y > self.scroll_y + self.visible_height:
            self.scroll_y = min(self.max_scroll, bottom_y - self.visible_height)

    def activar_opcion(self, index):
        nombre = self.items[index]["nombre"]
        if nombre.lower() == "salir":
            pygame.quit()
            sys.exit()
        else:
            mostrar_opcion(nombre)

# -------------------------------
# Programa principal
# -------------------------------
if __name__ == "__main__":
    menu = Menu(MENU_ITEMS)
    menu.run()
