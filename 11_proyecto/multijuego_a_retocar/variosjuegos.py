"""
Mini-colección de videojuegos en pygame + SQLite
- Menú navegable con ratón y teclado
- Juego 1: estilo "flappy" pero con control arriba/abajo (pasar huecos entre columnas)
- Juego 2: Snake clásico
- Juego 3: Marcianitos (simplificado)
- Opciones: editar nombre del jugador y cambiar control de movimiento (guardado en SQLite)

Requisitos:
- Python 3.8+
- pygame (pip install pygame)

Ejecutar:
python3 pygame_minijuegos.py

Archivo: single-file script
"""

import pygame
import sys
import random
import sqlite3
import os

# ----------------------------- Configuración y DB -----------------------------
DB_FILE = "settings.db"

DEFAULT_SETTINGS = {
    "name": "Jugador",
    "up_key": "K_UP",
    "down_key": "K_DOWN",
}

KEY_NAME_TO_CONST = {
    'K_UP': pygame.K_UP,
    'K_DOWN': pygame.K_DOWN,
    'K_LEFT': pygame.K_LEFT,
    'K_RIGHT': pygame.K_RIGHT,
    'K_w': pygame.K_w,
    'K_s': pygame.K_s,
    'K_a': pygame.K_a,
    'K_d': pygame.K_d,
}

KEY_CONST_TO_NAME = {v: k for k, v in KEY_NAME_TO_CONST.items()}


def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS settings (id INTEGER PRIMARY KEY, name TEXT, up_key TEXT, down_key TEXT)''')
    c.execute('SELECT COUNT(*) FROM settings')
    if c.fetchone()[0] == 0:
        c.execute('INSERT INTO settings (name, up_key, down_key) VALUES (?, ?, ?)',
                  (DEFAULT_SETTINGS['name'], DEFAULT_SETTINGS['up_key'], DEFAULT_SETTINGS['down_key']))
    conn.commit()
    conn.close()


def load_settings():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT name, up_key, down_key FROM settings WHERE id = 1')
    row = c.fetchone()
    conn.close()
    if row:
        name, up_key, down_key = row
        return {"name": name, "up_key": up_key, "down_key": down_key}
    else:
        return DEFAULT_SETTINGS.copy()


def save_settings(name, up_key, down_key):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('UPDATE settings SET name = ?, up_key = ?, down_key = ? WHERE id = 1', (name, up_key, down_key))
    conn.commit()
    conn.close()


# ----------------------------- Inicialización pygame -----------------------------
pygame.init()
SCREEN_W, SCREEN_H = 800, 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Mini-Juegos - Colección")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 28)
BIG_FONT = pygame.font.SysFont(None, 48)

init_db()
settings = load_settings()

# Helper: render texto

def render_text(text, font=FONT, color=(255,255,255)):
    return font.render(str(text), True, color)

# ----------------------------- Menú -----------------------------
MENU_ITEMS = ["Juego 1: Huecos", "Juego 2: Serpiente", "Juego 3: Marcianitos", "Opciones", "Salir"]


class Menu:
    def __init__(self):
        self.selected = 0

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
                        self.selected = (self.selected + 1) % len(MENU_ITEMS)
                    elif event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(MENU_ITEMS)
                    elif event.key == pygame.K_RETURN:
                        return self.activate_selected()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # click
                        for i, rect in enumerate(self.item_rects):
                            if rect.collidepoint(mouse_pos):
                                self.selected = i
                                return self.activate_selected()

            # draw
            screen.fill((20, 24, 30))
            title = BIG_FONT.render("Mini-Colección de Juegos", True, (255,255,255))
            screen.blit(title, (SCREEN_W//2 - title.get_width()//2, 40))

            self.item_rects = []
            for i, item in enumerate(MENU_ITEMS):
                txt = FONT.render(item, True, (255,255,255))
                rect = pygame.Rect(0, 0, 400, 40)
                rect.center = (SCREEN_W//2, 160 + i*60)
                self.item_rects.append(rect)
                color = (60, 120, 200) if i == self.selected else (80,80,80)
                pygame.draw.rect(screen, color, rect, border_radius=8)
                screen.blit(txt, (rect.x + 20, rect.y + 8))

            # show current player name
            name_surf = FONT.render(f"Jugador: {settings['name']}", True, (200,200,200))
            screen.blit(name_surf, (10, SCREEN_H - 30))

            # mouse hover selection
            for i, rect in enumerate(self.item_rects):
                if rect.collidepoint(mouse_pos):
                    self.selected = i

            pygame.display.flip()
            clock.tick(60)

    def activate_selected(self):
        choice = MENU_ITEMS[self.selected]
        if choice.startswith("Juego 1"):
            game1_loop()
        elif choice.startswith("Juego 2"):
            snake_loop()
        elif choice.startswith("Juego 3"):
            invaders_loop()
        elif choice == "Opciones":
            options_loop()
        elif choice == "Salir":
            pygame.quit()
            sys.exit()
        return None


# ----------------------------- Juego 1: Huecos (tipo Flappy pero arriba/abajo) -----------------------------

def game1_loop():
    # player rect
    player = pygame.Rect(120, SCREEN_H//2 - 15, 30, 30)
    vel = 0
    speed = 5
    gravity = 0.6
    gap_size = 180
    columns = []
    timer = 0
    score = 0
    font_big = pygame.font.SysFont(None, 36)

    # prepare key mapping
    up_const = KEY_NAME_TO_CONST.get(settings['up_key'], pygame.K_UP)
    down_const = KEY_NAME_TO_CONST.get(settings['down_key'], pygame.K_DOWN)

    running = True
    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        keys = pygame.key.get_pressed()
        if keys[up_const]:
            vel = -8
        elif keys[down_const]:
            vel = 8
        else:
            vel += gravity
            if vel > 8: vel = 8

        player.y += int(vel)
        # keep on screen
        if player.top < 0: player.top = 0; vel = 0
        if player.bottom > SCREEN_H: player.bottom = SCREEN_H; vel = 0

        # spawn columns
        timer += 1
        if timer > 90:
            timer = 0
            h = random.randint(80, SCREEN_H - 80 - gap_size)
            top_rect = pygame.Rect(SCREEN_W, 0, 70, h)
            bottom_rect = pygame.Rect(SCREEN_W, h + gap_size, 70, SCREEN_H - (h + gap_size))
            columns.append((top_rect, bottom_rect, False))

        # move columns
        for i in range(len(columns)):
            top, bottom, passed = columns[i]
            top.x -= 4
            bottom.x -= 4
            if not passed and top.right < player.left:
                # passed
                columns[i] = (top, bottom, True)
                score += 1

        # remove off-screen
        columns = [c for c in columns if c[0].right > -50]

        # collisions
        for top, bottom, _ in columns:
            if player.colliderect(top) or player.colliderect(bottom):
                # crash -> return to menu
                crash_message = font_big.render(f"Chocaste! Puntuación: {score}", True, (255,30,30))
                screen.blit(crash_message, (SCREEN_W//2 - crash_message.get_width()//2, SCREEN_H//2))
                pygame.display.flip()
                pygame.time.delay(1000)
                return

        # draw
        screen.fill((10, 15, 40))
        pygame.draw.rect(screen, (200,200,50), player)
        for top, bottom, _ in columns:
            pygame.draw.rect(screen, (50,200,50), top)
            pygame.draw.rect(screen, (50,200,50), bottom)

        score_surf = FONT.render(f"Puntuación: {score}", True, (255,255,255))
        screen.blit(score_surf, (10, 10))
        info_surf = FONT.render(f"Controles: {settings['up_key']} / {settings['down_key']}  - ESC para volver", True, (180,180,180))
        screen.blit(info_surf, (10, SCREEN_H-30))

        pygame.display.flip()


# ----------------------------- Juego 2: Serpiente -----------------------------

def snake_loop():
    grid_size = 20
    cols = SCREEN_W // grid_size
    rows = SCREEN_H // grid_size
    snake = [(cols//2, rows//2)]
    dir = (1,0)
    food = (random.randint(0, cols-1), random.randint(0, rows-1))
    speed = 8
    score = 0

    up_const = KEY_NAME_TO_CONST.get(settings['up_key'], pygame.K_UP)
    down_const = KEY_NAME_TO_CONST.get(settings['down_key'], pygame.K_DOWN)

    # interpret settings: we'll let user use up/down mapped to turn snake up/down relative to current dir
    # but for simplicity also allow arrow keys alternative

    last_move_time = 0
    running = True
    while running:
        dt = clock.tick(60)
        last_move_time += dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                # standard snake keys
                if event.key == pygame.K_UP and dir != (0,1): dir = (0,-1)
                elif event.key == pygame.K_DOWN and dir != (0,-1): dir = (0,1)
                elif event.key == pygame.K_LEFT and dir != (1,0): dir = (-1,0)
                elif event.key == pygame.K_RIGHT and dir != (-1,0): dir = (1,0)
                # also allow configured up/down to move vertically
                elif event.key == up_const and dir != (0,1): dir = (0,-1)
                elif event.key == down_const and dir != (0,-1): dir = (0,1)

        if last_move_time > 1000//speed:
            last_move_time = 0
            head = (snake[0][0] + dir[0], snake[0][1] + dir[1])
            # wrap-around
            head = (head[0] % cols, head[1] % rows)
            if head in snake:
                # dead
                pygame.time.delay(500)
                return
            snake.insert(0, head)
            if head == food:
                score += 1
                # place food not on snake
                while True:
                    food = (random.randint(0, cols-1), random.randint(0, rows-1))
                    if food not in snake:
                        break
            else:
                snake.pop()

        screen.fill((12, 12, 12))
        # draw food
        pygame.draw.rect(screen, (200,50,50), (food[0]*grid_size, food[1]*grid_size, grid_size, grid_size))
        # draw snake
        for i, seg in enumerate(snake):
            color = (50,200,50) if i==0 else (50,120,50)
            pygame.draw.rect(screen, color, (seg[0]*grid_size, seg[1]*grid_size, grid_size, grid_size))

        score_surf = FONT.render(f"Puntuación: {score}", True, (255,255,255))
        screen.blit(score_surf, (10, 10))
        info_surf = FONT.render("Flechas o controles personalizados - ESC para volver", True, (180,180,180))
        screen.blit(info_surf, (10, SCREEN_H-30))

        pygame.display.flip()


# ----------------------------- Juego 3: Marcianitos (simplificado) -----------------------------

def invaders_loop():
    player = pygame.Rect(SCREEN_W//2 - 20, SCREEN_H - 60, 40, 30)
    bullets = []
    enemies = []
    enemy_rows = 3
    enemy_cols = 8
    for r in range(enemy_rows):
        for c in range(enemy_cols):
            enemies.append(pygame.Rect(80 + c*70, 50 + r*50, 40, 30))
    enemy_dir = 1
    enemy_speed = 0.4
    enemy_timer = 0
    player_speed = 6
    score = 0

    running = True
    while running:
        dt = clock.tick(60)
        enemy_timer += dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_SPACE:
                    bullets.append(pygame.Rect(player.centerx-3, player.top-10, 6, 12))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
        player.x = max(0, min(SCREEN_W - player.width, player.x))

        # move bullets
        for b in bullets:
            b.y -= 10
        bullets = [b for b in bullets if b.y > -20]

        # move enemies slowly
        if enemy_timer > 30:
            enemy_timer = 0
            shift_x = enemy_dir
            for e in enemies:
                e.x += shift_x
            # if any out of bounds flip and descend
            leftmost = min(e.x for e in enemies) if enemies else 0
            rightmost = max(e.x for e in enemies) + (enemies[0].width if enemies else 0)
            if leftmost < 10 or rightmost > SCREEN_W - 10:
                enemy_dir *= -1
                for e in enemies:
                    e.y += 10

        # collision bullets vs enemies
        for b in bullets[:]:
            for e in enemies[:]:
                if b.colliderect(e):
                    bullets.remove(b)
                    enemies.remove(e)
                    score += 10
                    break

        # if enemies reach player -> game over
        for e in enemies:
            if e.colliderect(player) or e.bottom >= SCREEN_H - 50:
                # explosion & return
                msg = BIG_FONT.render(f"Derrotado! Puntuación: {score}", True, (255,40,40))
                screen.blit(msg, (SCREEN_W//2 - msg.get_width()//2, SCREEN_H//2))
                pygame.display.flip()
                pygame.time.delay(800)
                return

        # win if no enemies
        if not enemies:
            msg = BIG_FONT.render(f"Victoria! Puntuación: {score}", True, (80,255,80))
            screen.blit(msg, (SCREEN_W//2 - msg.get_width()//2, SCREEN_H//2))
            pygame.display.flip()
            pygame.time.delay(800)
            return

        # draw
        screen.fill((0, 0, 20))
        pygame.draw.rect(screen, (50,200,200), player)
        for b in bullets:
            pygame.draw.rect(screen, (255,255,100), b)
        for e in enemies:
            pygame.draw.rect(screen, (200,80,80), e)

        score_surf = FONT.render(f"Puntuación: {score}", True, (255,255,255))
        screen.blit(score_surf, (10, 10))
        info_surf = FONT.render("Flechas para mover, ESPACIO para disparar, ESC para volver", True, (180,180,180))
        screen.blit(info_surf, (10, SCREEN_H-30))

        pygame.display.flip()


# ----------------------------- Opciones -----------------------------

def options_loop():
    # simple UI: input box for name + buttons to choose control scheme + "guardar" button
    global settings
    input_active = False
    input_text = settings['name']
    selected_scheme = (settings['up_key'], settings['down_key'])
    message = ''

    # rectangle definitions
    name_rect = pygame.Rect(SCREEN_W//2 - 200, 140, 400, 40)
    arrow_btn = pygame.Rect(SCREEN_W//2 - 200, 210, 180, 40)
    ws_btn = pygame.Rect(SCREEN_W//2 + 20, 210, 180, 40)
    custom_btn = pygame.Rect(SCREEN_W//2 - 200, 270, 400, 40)
    save_btn = pygame.Rect(SCREEN_W//2 - 80, 340, 160, 40)

    # custom flag
    waiting_custom = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if waiting_custom:
                    # register pressed key as up or down depending on stage
                    # We'll capture two sequential keys: first will be up, second down
                    if 'custom_tmp' not in locals():
                        custom_tmp = [event.key]
                        message = 'Pulsa la tecla para DOWN'
                    else:
                        custom_tmp.append(event.key)
                        # map to names (try to convert into known names or generic)
                        up_name = KEY_CONST_TO_NAME.get(custom_tmp[0], pygame.key.name(custom_tmp[0]).upper())
                        down_name = KEY_CONST_TO_NAME.get(custom_tmp[1], pygame.key.name(custom_tmp[1]).upper())
                        # normalize to 'K_x' naming used in settings
                        up_key_str = f'K_{pygame.key.name(custom_tmp[0])}'.replace(' ', '_')
                        down_key_str = f'K_{pygame.key.name(custom_tmp[1])}'.replace(' ', '_')
                        # store
                        selected_scheme = (up_key_str, down_key_str)
                        waiting_custom = False
                        del custom_tmp
                        message = 'Controles personalizados asignados (guardar para aplicar)'
                elif input_active:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        input_active = False
                    else:
                        # limit name length
                        if len(input_text) < 20:
                            input_text += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = event.pos
                    if name_rect.collidepoint(mx, my):
                        input_active = True
                    else:
                        input_active = False
                    if arrow_btn.collidepoint(mx, my):
                        selected_scheme = ('K_UP', 'K_DOWN')
                        message = 'Usando flechas ARRIBA/ABAJO'
                    elif ws_btn.collidepoint(mx, my):
                        selected_scheme = ('K_w', 'K_s')
                        message = 'Usando W / S'
                    elif custom_btn.collidepoint(mx, my):
                        waiting_custom = True
                        message = 'Pulsa la tecla para UP'
                    elif save_btn.collidepoint(mx, my):
                        # save into DB
                        # normalize selected_scheme values
                        up_s, down_s = selected_scheme
                        try:
                            save_settings(input_text if input_text.strip()!='' else DEFAULT_SETTINGS['name'], up_s, down_s)
                            # reload into settings
                            #global settings
                            settings = load_settings()
                            message = 'Guardado correctamente.'
                        except Exception as e:
                            message = 'Error guardando: ' + str(e)

        # draw
        screen.fill((28, 30, 40))
        title = BIG_FONT.render('Opciones', True, (255,255,255))
        screen.blit(title, (SCREEN_W//2 - title.get_width()//2, 40))

        # name box
        pygame.draw.rect(screen, (60,60,60), name_rect, border_radius=6)
        name_surf = FONT.render(input_text if input_text else 'Introduce nombre...', True, (255,255,255))
        screen.blit(name_surf, (name_rect.x + 8, name_rect.y + 8))

        # scheme buttons
        pygame.draw.rect(screen, (80,120,160) if selected_scheme==('K_UP','K_DOWN') else (60,60,60), arrow_btn, border_radius=6)
        screen.blit(FONT.render('Flechas Arriba/Abajo', True, (255,255,255)), (arrow_btn.x+8, arrow_btn.y+8))
        pygame.draw.rect(screen, (80,120,160) if selected_scheme==('K_w','K_s') else (60,60,60), ws_btn, border_radius=6)
        screen.blit(FONT.render('W / S', True, (255,255,255)), (ws_btn.x+8, ws_btn.y+8))

        pygame.draw.rect(screen, (70,70,100), custom_btn, border_radius=6)
        screen.blit(FONT.render('Teclas Personalizadas (pulsa para asignar)', True, (255,255,255)), (custom_btn.x+8, custom_btn.y+8))

        pygame.draw.rect(screen, (120,180,100), save_btn, border_radius=6)
        screen.blit(FONT.render('Guardar', True, (0,0,0)), (save_btn.x+36, save_btn.y+8))

        # show current selection
        csurf = FONT.render(f"Seleccionado: {selected_scheme[0]} / {selected_scheme[1]}", True, (200,200,200))
        screen.blit(csurf, (SCREEN_W//2 - csurf.get_width()//2, 400))

        msgsurf = FONT.render(message, True, (200,200,80))
        screen.blit(msgsurf, (SCREEN_W//2 - msgsurf.get_width()//2, 430))

        hint = FONT.render('Presiona ESC para volver al menú', True, (150,150,150))
        screen.blit(hint, (10, SCREEN_H-30))

        pygame.display.flip()
        clock.tick(60)


# ----------------------------- Main loop -----------------------------

def main():
    menu = Menu()
    while True:
        menu.run()


if __name__ == '__main__':
    main()
