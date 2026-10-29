"""
generate_graphics.py - Generador de ilustraciones vectoriales/rasterizadas en alta resolución
Utiliza Pillow con supersampling 4x (LANCZOS) y paleta acuarela del Bosque de los Cien Acres.
Genera:
1. gift_closed.png: Caja de regalo con lazo rojo satinado y etiqueta "Para Ti ♡"
2. gift_opened.png: Caja abierta con partículas de corazones y resplandor
3. pooh_greeting.png: Pose 1 - Pooh saludando con una patita arriba
4. pooh_thinking.png: Pose 2 - Pooh pensando con el dedo en la sien ("Think, think, think...")
5. pooh_honey.png: Pose 3 - Pooh abrazando su tarro de "HUNNY" con miel dorada
6. pooh_balloon.png: Pose 4 - Pooh flotando con su clásico globo rojo
7. pooh_hug.png: Pose 5 - Pooh abrazando un corazón tierno
8. pooh_resting.png: Pose 6 - Pooh sentado con una mariposa en la patita
9. honey_pot.png: Tarrito de miel para la carta secreta
10. icon.ico: Ícono oficial para el ejecutable
"""

import math
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSETS_DIR = r"C:\Users\LENOVO\.gemini\antigravity\scratch\winnie_pooh_gift\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Paleta clásica Winnie the Pooh
COLOR_POOH_GOLD = (245, 188, 55, 255)
COLOR_POOH_SHADOW = (220, 160, 40, 255)
COLOR_POOH_HIGHLIGHT = (255, 210, 95, 255)
COLOR_SHIRT_RED = (215, 48, 48, 255)
COLOR_SHIRT_DARK = (180, 30, 30, 255)
COLOR_NOSE_BLACK = (45, 30, 25, 255)
COLOR_EYE_BLACK = (35, 25, 20, 255)
COLOR_CHEEK_PINK = (255, 160, 160, 110)
COLOR_HONEY_POT = (185, 125, 80, 255)
COLOR_HONEY_POT_DARK = (150, 95, 55, 255)
COLOR_HONEY_GOLD = (255, 200, 30, 255)
COLOR_HEART_RED = (235, 65, 85, 255)
COLOR_BALLOON_RED = (230, 45, 55, 255)

SCALE = 4  # 4x Supersampling para acabado suave
TARGET_SIZE = 512
CANVAS_SIZE = TARGET_SIZE * SCALE  # 2048x2048

def create_super_canvas():
    return Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))

def finalize_image(img, filepath):
    # Downsample suave con LANCZOS
    res = img.resize((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)
    res.save(filepath, "PNG")

def draw_pooh_head(draw, cx, cy, r, eye_state="open", smile_type="happy", tilt_deg=0):
    """Dibuja la cabeza y rostro inconfundible de Pooh"""
    # Oreja izquierda
    ear_r = r * 0.38
    draw.ellipse([cx - r * 0.85, cy - r * 0.95, cx - r * 0.85 + ear_r * 2, cy - r * 0.95 + ear_r * 2], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx - r * 0.78, cy - r * 0.88, cx - r * 0.78 + ear_r * 1.5, cy - r * 0.88 + ear_r * 1.5], fill=COLOR_POOH_SHADOW)
    
    # Oreja derecha
    draw.ellipse([cx + r * 0.85 - ear_r * 2, cy - r * 0.95, cx + r * 0.85, cy - r * 0.95 + ear_r * 2], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + r * 0.78 - ear_r * 1.5, cy - r * 0.88, cx + r * 0.78, cy - r * 0.88 + ear_r * 1.5], fill=COLOR_POOH_SHADOW)
    
    # Cabeza redonda tierna
    draw.ellipse([cx - r, cy - r * 0.9, cx + r, cy + r * 0.9], fill=COLOR_POOH_GOLD)
    
    # Mejillas redondas inferiores (forma pera de Pooh)
    draw.ellipse([cx - r * 0.95, cy, cx + r * 0.95, cy + r * 0.95], fill=COLOR_POOH_GOLD)
    
    # Hocico sobresaliente
    snout_rx = r * 0.55
    snout_ry = r * 0.42
    snout_y = cy + r * 0.28
    draw.ellipse([cx - snout_rx, snout_y - snout_ry, cx + snout_rx, snout_y + snout_ry], fill=COLOR_POOH_HIGHLIGHT)
    
    # Nariz suave ovalada
    nose_rx = r * 0.22
    nose_ry = r * 0.16
    nose_y = snout_y - r * 0.14
    draw.ellipse([cx - nose_rx, nose_y - nose_ry, cx + nose_rx, nose_y + nose_ry], fill=COLOR_NOSE_BLACK)
    # Brillo en la nariz
    draw.ellipse([cx - nose_rx * 0.4, nose_y - nose_ry * 0.5, cx, nose_y - nose_ry * 0.1], fill=(255, 255, 255, 200))
    
    # Sonrojo en mejillas
    draw.ellipse([cx - r * 0.75, cy + r * 0.2, cx - r * 0.35, cy + r * 0.55], fill=COLOR_CHEEK_PINK)
    draw.ellipse([cx + r * 0.35, cy + r * 0.2, cx + r * 0.75, cy + r * 0.55], fill=COLOR_CHEEK_PINK)
    
    # Ojos
    eye_y = cy - r * 0.08
    eye_spacing = r * 0.38
    if eye_state == "open":
        eye_r = r * 0.11
        # Izquierdo
        draw.ellipse([cx - eye_spacing - eye_r, eye_y - eye_r, cx - eye_spacing + eye_r, eye_y + eye_r], fill=COLOR_EYE_BLACK)
        draw.ellipse([cx - eye_spacing - eye_r * 0.3, eye_y - eye_r * 0.4, cx - eye_spacing + eye_r * 0.2, eye_y], fill=(255, 255, 255, 220))
        # Derecho
        draw.ellipse([cx + eye_spacing - eye_r, eye_y - eye_r, cx + eye_spacing + eye_r, eye_y + eye_r], fill=COLOR_EYE_BLACK)
        draw.ellipse([cx + eye_spacing - eye_r * 0.3, eye_y - eye_r * 0.4, cx + eye_spacing + eye_r * 0.2, eye_y], fill=(255, 255, 255, 220))
        # Cejitas tiernas levantadas
        draw.arc([cx - eye_spacing - eye_r * 1.4, eye_y - eye_r * 2.2, cx - eye_spacing + eye_r * 1.4, eye_y - eye_r * 0.6], 200, 340, fill=COLOR_NOSE_BLACK, width=int(SCALE * 3.5))
        draw.arc([cx + eye_spacing - eye_r * 1.4, eye_y - eye_r * 2.2, cx + eye_spacing + eye_r * 1.4, eye_y - eye_r * 0.6], 200, 340, fill=COLOR_NOSE_BLACK, width=int(SCALE * 3.5))
    elif eye_state == "closed_happy":
        # Curvitas de ojos cerrados de felicidad ^ ^
        arc_w = int(SCALE * 5)
        draw.arc([cx - eye_spacing - r * 0.16, eye_y - r * 0.12, cx - eye_spacing + r * 0.16, eye_y + r * 0.12], 200, 340, fill=COLOR_NOSE_BLACK, width=arc_w)
        draw.arc([cx + eye_spacing - r * 0.16, eye_y - r * 0.12, cx + eye_spacing + r * 0.16, eye_y + r * 0.12], 200, 340, fill=COLOR_NOSE_BLACK, width=arc_w)
    
    # Sonrisa
    mouth_y = snout_y + r * 0.08
    draw.arc([cx - r * 0.26, mouth_y - r * 0.14, cx + r * 0.26, mouth_y + r * 0.2], 20, 160, fill=COLOR_NOSE_BLACK, width=int(SCALE * 4))

def draw_pooh_body_base(draw, cx, cy, w, h):
    """Cuerpo tierno y barriguita de Pooh"""
    # Barriga suave
    draw.ellipse([cx - w * 0.5, cy - h * 0.3, cx + w * 0.5, cy + h * 0.7], fill=COLOR_POOH_GOLD)
    # Camiseta roja clásica corta
    draw.ellipse([cx - w * 0.52, cy - h * 0.35, cx + w * 0.52, cy + h * 0.25], fill=COLOR_SHIRT_RED)
    # Cuellito de camisa
    draw.arc([cx - w * 0.25, cy - h * 0.42, cx + w * 0.25, cy - h * 0.15], 10, 170, fill=COLOR_SHIRT_DARK, width=int(SCALE * 4))

# ----------------- GENERADORES ESPECÍFICOS DE POSES -----------------

def gen_gift_closed():
    img = create_super_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_SIZE // 2, CANVAS_SIZE // 2 + 100
    bw, bh = 850, 750
    
    # Sombra suave en el piso
    draw.ellipse([cx - 500, cy + bh // 2 - 20, cx + 500, cy + bh // 2 + 160], fill=(0, 0, 0, 35))
    
    # Caja de regalo (colores crema pastel cálido)
    bx0, by0, bx1, by1 = cx - bw // 2, cy - bh // 2 + 120, cx + bw // 2, cy + bh // 2 + 50
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=60, fill=(255, 248, 225, 255), outline=(230, 210, 170, 255), width=int(SCALE * 3))
    
    # Tapa de la caja (ligeramente más ancha)
    lid_h = 170
    draw.rounded_rectangle([bx0 - 35, by0 - 80, bx1 + 35, by0 + lid_h - 80], radius=40, fill=(255, 238, 195, 255), outline=(225, 195, 140, 255), width=int(SCALE * 3))
    
    # Cinta vertical roja satinada
    rib_w = 140
    draw.rectangle([cx - rib_w // 2, by0 - 80, cx + rib_w // 2, by1], fill=COLOR_SHIRT_RED)
    draw.rectangle([cx - rib_w // 2 + 25, by0 - 80, cx - rib_w // 2 + 45, by1], fill=(255, 120, 120, 200)) # Brillo
    
    # Cinta horizontal en la tapa
    draw.rectangle([bx0 - 35, by0 - 15, bx1 + 35, by0 + 75], fill=COLOR_SHIRT_RED)
    
    # Lazo superior grande y tierno
    bow_y = by0 - 110
    # Lazo izquierdo
    draw.ellipse([cx - 300, bow_y - 120, cx - 20, bow_y + 80], fill=COLOR_SHIRT_RED)
    draw.ellipse([cx - 240, bow_y - 80, cx - 70, bow_y + 40], fill=(255, 238, 195, 255)) # Hueco
    # Lazo derecho
    draw.ellipse([cx + 20, bow_y - 120, cx + 300, bow_y + 80], fill=COLOR_SHIRT_RED)
    draw.ellipse([cx + 70, bow_y - 80, cx + 240, bow_y + 40], fill=(255, 238, 195, 255))
    # Nudo central
    draw.ellipse([cx - 70, bow_y - 50, cx + 70, bow_y + 60], fill=COLOR_SHIRT_DARK)
    
    # Cintas colgantes
    draw.polygon([(cx - 40, bow_y + 40), (cx - 160, bow_y + 280), (cx - 100, bow_y + 270), (cx, bow_y + 50)], fill=COLOR_SHIRT_RED)
    draw.polygon([(cx + 40, bow_y + 40), (cx + 160, bow_y + 280), (cx + 100, bow_y + 270), (cx, bow_y + 50)], fill=COLOR_SHIRT_RED)
    
    # Etiqueta de regalo tierna colgando "Para Ti ♡"
    tag_x, tag_y = cx + 220, cy + 60
    draw.rounded_rectangle([tag_x - 120, tag_y - 70, tag_x + 120, tag_y + 70], radius=25, fill=(255, 255, 255, 245), outline=COLOR_SHIRT_RED, width=int(SCALE * 2))
    draw.ellipse([tag_x - 100, tag_y - 15, tag_x - 70, tag_y + 15], fill=(200, 200, 200, 255)) # Ojal
    # Pequeño corazón en la etiqueta
    draw.ellipse([tag_x + 30, tag_y - 25, tag_x + 60, tag_y + 5], fill=COLOR_HEART_RED)
    draw.ellipse([tag_x + 50, tag_y - 25, tag_x + 80, tag_y + 5], fill=COLOR_HEART_RED)
    draw.polygon([(tag_x + 30, tag_y - 5), (tag_x + 80, tag_y - 5), (tag_x + 55, tag_y + 25)], fill=COLOR_HEART_RED)
    
    finalize_image(img, os.path.join(ASSETS_DIR, "gift_closed.png"))

def gen_gift_opened():
    img = create_super_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_SIZE // 2, CANVAS_SIZE // 2 + 250
    bw, bh = 850, 480
    
    # Sombra
    draw.ellipse([cx - 520, cy + bh // 2 - 20, cx + 520, cy + bh // 2 + 150], fill=(0, 0, 0, 30))
    # Caja abierta vista en perspectiva
    bx0, by0, bx1, by1 = cx - bw // 2, cy - bh // 2, cx + bw // 2, cy + bh // 2
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=50, fill=(255, 248, 225, 255), outline=(230, 210, 170, 255), width=int(SCALE * 3))
    # Interior oscuro suave
    draw.ellipse([bx0 + 30, by0 - 70, bx1 - 30, by0 + 90], fill=(235, 215, 170, 255))
    
    # Destellos, estrellas y corazones flotando mágicamente
    sparks = [
        (cx - 320, cy - 450, 45, COLOR_HEART_RED),
        (cx + 340, cy - 400, 50, COLOR_HONEY_GOLD),
        (cx - 180, cy - 580, 60, COLOR_HONEY_GOLD),
        (cx + 190, cy - 620, 55, COLOR_HEART_RED),
        (cx - 400, cy - 250, 35, COLOR_HONEY_GOLD),
        (cx + 390, cy - 200, 40, COLOR_HEART_RED),
    ]
    for sx, sy, sr, col in sparks:
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=col)
        # Cruz de brillo
        draw.line([(sx - sr * 1.5, sy), (sx + sr * 1.5, sy)], fill=(255, 255, 255, 220), width=int(SCALE * 2.5))
        draw.line([(sx, sy - sr * 1.5), (sx, sy + sr * 1.5)], fill=(255, 255, 255, 220), width=int(SCALE * 2.5))

    finalize_image(img, os.path.join(ASSETS_DIR, "gift_opened.png"))

def gen_pooh_greeting():
    """Pose 1: Saludando con patita levantada y sonrisa cálida"""
    img = create_super_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_SIZE // 2, CANVAS_SIZE // 2 + 60
    
    # Sombra en piso
    draw.ellipse([cx - 320, cy + 680, cx + 320, cy + 790], fill=(0, 0, 0, 25))
    
    # Patitas inferiores
    draw.ellipse([cx - 260, cy + 540, cx - 80, cy + 740], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 80, cy + 540, cx + 260, cy + 740], fill=COLOR_POOH_GOLD)
    
    # Cuerpo
    draw_pooh_body_base(draw, cx, cy + 240, 680, 720)
    
    # Brazo izquierdo relajado abajo
    draw.ellipse([cx - 380, cy + 220, cx - 220, cy + 500], fill=COLOR_POOH_GOLD)
    # Manga roja
    draw.ellipse([cx - 380, cy + 180, cx - 240, cy + 340], fill=COLOR_SHIRT_RED)
    
    # Brazo derecho levantado saludando (Waving paw)
    draw.ellipse([cx + 230, cy - 60, cx + 390, cy + 280], fill=COLOR_POOH_GOLD)
    # Patita redonda
    draw.ellipse([cx + 250, cy - 140, cx + 410, cy + 40], fill=COLOR_POOH_GOLD)
    # Manga derecha
    draw.ellipse([cx + 200, cy + 180, cx + 340, cy + 340], fill=COLOR_SHIRT_RED)
    
    # Cabeza
    draw_pooh_head(draw, cx, cy - 180, 270, eye_state="open", smile_type="happy")
    
    finalize_image(img, os.path.join(ASSETS_DIR, "pooh_greeting.png"))

def gen_pooh_thinking():
    """Pose 2: Pensando con dedo en la cabeza ('Think, think, think...')"""
    img = create_super_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_SIZE // 2, CANVAS_SIZE // 2 + 80
    
    # Sombra
    draw.ellipse([cx - 340, cy + 660, cx + 340, cy + 770], fill=(0, 0, 0, 25))
    # Patitas sentadas adelante
    draw.ellipse([cx - 310, cy + 500, cx - 110, cy + 700], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 110, cy + 500, cx + 310, cy + 700], fill=COLOR_POOH_GOLD)
    
    # Cuerpo
    draw_pooh_body_base(draw, cx, cy + 250, 690, 700)
    
    # Brazo izquierdo sobre la rodilla
    draw.ellipse([cx - 360, cy + 280, cx - 200, cy + 540], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx - 360, cy + 200, cx - 220, cy + 350], fill=COLOR_SHIRT_RED)
    
    # Brazo derecho doblado hacia la cabeza (tocando sien)
    draw.ellipse([cx + 170, cy + 10, cx + 350, cy + 260], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 160, cy - 100, cx + 290, cy + 60], fill=COLOR_POOH_GOLD) # Mano en sien
    draw.ellipse([cx + 200, cy + 190, cx + 340, cy + 340], fill=COLOR_SHIRT_RED)
    
    # Cabeza ligeramente inclinada
    draw_pooh_head(draw, cx - 20, cy - 170, 270, eye_state="open", smile_type="pensive")
    
    # Nube de pensamiento tierno con tarro de miel flotando
    bx, by = cx + 380, cy - 420
    draw.ellipse([bx - 120, by - 80, bx + 120, by + 80], fill=(255, 255, 255, 230), outline=(230, 210, 170, 255), width=int(SCALE * 2))
    draw.ellipse([bx - 140, by + 120, bx - 100, by + 160], fill=(255, 255, 255, 230))
    draw.ellipse([bx - 80, by + 80, bx - 50, by + 110], fill=(255, 255, 255, 230))
    # Pequeño tarrito de miel adentro del pensamiento
    draw.rounded_rectangle([bx - 40, by - 30, bx + 40, by + 40], radius=15, fill=COLOR_HONEY_POT)
    draw.ellipse([bx - 45, by - 40, bx + 45, by - 20], fill=COLOR_HONEY_GOLD)
    
    finalize_image(img, os.path.join(ASSETS_DIR, "pooh_thinking.png"))

def gen_pooh_honey():
    """Pose 3: Abrazando feliz su gran tarro de HUNNY"""
    img = create_super_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_SIZE // 2, CANVAS_SIZE // 2 + 90
    
    # Sombra
    draw.ellipse([cx - 360, cy + 650, cx + 360, cy + 770], fill=(0, 0, 0, 25))
    # Patitas gorditas abiertas sentadas
    draw.ellipse([cx - 370, cy + 460, cx - 180, cy + 680], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 180, cy + 460, cx + 370, cy + 680], fill=COLOR_POOH_GOLD)
    # Almohadillas marrones
    draw.ellipse([cx - 330, cy + 520, cx - 220, cy + 630], fill=COLOR_POOH_SHADOW)
    draw.ellipse([cx + 220, cy + 520, cx + 330, cy + 630], fill=COLOR_POOH_SHADOW)
    
    # Cuerpo
    draw_pooh_body_base(draw, cx, cy + 230, 680, 680)
    
    # GRAN TARRO DE MIEL EN EL CENTRO
    pot_y = cy + 340
    pw, ph = 460, 420
    draw.rounded_rectangle([cx - pw // 2, pot_y - ph // 2, cx + pw // 2, pot_y + ph // 2], radius=60, fill=COLOR_HONEY_POT, outline=COLOR_HONEY_POT_DARK, width=int(SCALE * 3))
    # Borde superior del tarro
    draw.ellipse([cx - pw // 2 - 20, pot_y - ph // 2 - 40, cx + pw // 2 + 20, pot_y - ph // 2 + 50], fill=COLOR_HONEY_POT_DARK)
    draw.ellipse([cx - pw // 2 - 10, pot_y - ph // 2 - 30, cx + pw // 2 + 10, pot_y - ph // 2 + 40], fill=COLOR_HONEY_GOLD) # Miel dorada desbordándose
    # Gotas de miel escurriendo
    draw.rounded_rectangle([cx - 100, pot_y - ph // 2 + 20, cx - 40, pot_y - ph // 2 + 160], radius=25, fill=COLOR_HONEY_GOLD)
    draw.rounded_rectangle([cx + 60, pot_y - ph // 2 + 20, cx + 110, pot_y - ph // 2 + 120], radius=25, fill=COLOR_HONEY_GOLD)
    
    # Texto 'HUNNY' estilo rústico de Pooh
    draw.rounded_rectangle([cx - 130, pot_y - 20, cx + 130, pot_y + 80], radius=20, fill=(245, 235, 210, 240))
    # Letras simuladas H U N N Y con trazo oscuro infantil
    draw.line([(cx - 100, pot_y), (cx - 100, pot_y + 60)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 3))
    draw.line([(cx - 75, pot_y), (cx - 75, pot_y + 60)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 3))
    draw.line([(cx - 100, pot_y + 30), (cx - 75, pot_y + 30)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 3)) # H
    draw.arc([cx - 50, pot_y, cx - 15, pot_y + 60], 0, 180, fill=COLOR_NOSE_BLACK, width=int(SCALE * 3)) # U
    draw.line([(cx + 5, pot_y), (cx + 5, pot_y + 60)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 3))
    draw.line([(cx + 5, pot_y), (cx + 35, pot_y + 60)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 3))
    draw.line([(cx + 35, pot_y), (cx + 35, pot_y + 60)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 3)) # N
    draw.line([(cx + 60, pot_y), (cx + 75, pot_y + 30)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 3))
    draw.line([(cx + 90, pot_y), (cx + 75, pot_y + 30)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 3))
    draw.line([(cx + 75, pot_y + 30), (cx + 75, pot_y + 60)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 3)) # Y
    
    # Brazos de Pooh abrazando el tarro por los costados
    draw.ellipse([cx - 360, cy + 220, cx - 140, cy + 460], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 140, cy + 220, cx + 360, cy + 460], fill=COLOR_POOH_GOLD)
    # Mangas
    draw.ellipse([cx - 340, cy + 180, cx - 210, cy + 320], fill=COLOR_SHIRT_RED)
    draw.ellipse([cx + 210, cy + 180, cx + 340, cy + 320], fill=COLOR_SHIRT_RED)
    
    # Cabeza con ojos cerrados de felicidad comiendo miel
    draw_pooh_head(draw, cx, cy - 180, 270, eye_state="closed_happy", smile_type="very_happy")
    # Mancha de miel dorada en la mejilla
    draw.ellipse([cx + 60, cy - 100, cx + 110, cy - 60], fill=COLOR_HONEY_GOLD)
    
    finalize_image(img, os.path.join(ASSETS_DIR, "pooh_honey.png"))

def gen_pooh_balloon():
    """Pose 4: Flotando sostenido de su globo rojo clásico"""
    img = create_super_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_SIZE // 2, CANVAS_SIZE // 2 + 180
    
    # Globo rojo arriba
    ball_x, ball_y = cx, cy - 700
    bw, bh = 420, 500
    draw.ellipse([ball_x - bw // 2, ball_y - bh // 2, ball_x + bw // 2, ball_y + bh // 2], fill=COLOR_BALLOON_RED)
    # Reflejo curvo blanco del globo
    draw.arc([ball_x - bw // 2 + 40, ball_y - bh // 2 + 40, ball_x - bw // 2 + 140, ball_y - bh // 2 + 200], 120, 260, fill=(255, 255, 255, 180), width=int(SCALE * 5))
    # Nudo del globo
    draw.polygon([(ball_x - 30, ball_y + bh // 2), (ball_x + 30, ball_y + bh // 2), (ball_x, ball_y + bh // 2 + 40)], fill=COLOR_SHIRT_DARK)
    
    # Hilo del globo bajando a la mano de Pooh
    hand_y = cy - 280
    draw.line([(ball_x, ball_y + bh // 2 + 35), (cx + 80, hand_y)], fill=(120, 110, 100, 255), width=int(SCALE * 2.5))
    
    # Patitas colgando libres en el aire (flotando)
    draw.ellipse([cx - 220, cy + 380, cx - 80, cy + 590], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 40, cy + 390, cx + 180, cy + 600], fill=COLOR_POOH_GOLD)
    
    # Cuerpo flotante
    draw_pooh_body_base(draw, cx, cy + 120, 620, 640)
    
    # Brazo izquierdo abierto equilibrándose
    draw.ellipse([cx - 340, cy + 60, cx - 180, cy + 320], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx - 320, cy + 70, cx - 190, cy + 220], fill=COLOR_SHIRT_RED)
    
    # Brazo derecho estirado hacia arriba agarrando el hilo
    draw.ellipse([cx + 60, hand_y - 40, cx + 220, cy + 180], fill=COLOR_POOH_GOLD)
    # Mano cerrada sobre el hilo
    draw.ellipse([cx + 50, hand_y - 60, cx + 120, hand_y + 20], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 120, cy + 50, cx + 240, cy + 200], fill=COLOR_SHIRT_RED)
    
    # Cabeza mirando con asombro y sonrisa
    draw_pooh_head(draw, cx, cy - 180, 260, eye_state="open", smile_type="happy")
    
    # Pequeña nubecita suave de fondo
    draw.ellipse([cx - 350, cy + 50, cx - 150, cy + 170], fill=(255, 255, 255, 80))
    draw.ellipse([cx + 200, cy + 20, cx + 420, cy + 140], fill=(255, 255, 255, 80))
    
    finalize_image(img, os.path.join(ASSETS_DIR, "pooh_balloon.png"))

def gen_pooh_hug():
    """Pose 5: Abrazando un corazón con dulzura y ojos cerrados"""
    img = create_super_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_SIZE // 2, CANVAS_SIZE // 2 + 70
    
    # Sombra
    draw.ellipse([cx - 320, cy + 650, cx + 320, cy + 760], fill=(0, 0, 0, 25))
    # Patitas sentadas
    draw.ellipse([cx - 290, cy + 500, cx - 100, cy + 690], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 100, cy + 500, cx + 290, cy + 690], fill=COLOR_POOH_GOLD)
    
    # Cuerpo
    draw_pooh_body_base(draw, cx, cy + 240, 680, 690)
    
    # GRAN CORAZÓN ROJO EN EL PECHO
    hx, hy = cx, cy + 260
    hr = 170
    draw.ellipse([hx - hr - 10, hy - hr, hx, hy + 30], fill=COLOR_HEART_RED)
    draw.ellipse([hx, hy - hr, hx + hr + 10, hy + 30], fill=COLOR_HEART_RED)
    draw.polygon([(hx - hr - 10, hy - 40), (hx + hr + 10, hy - 40), (hx, hy + hr + 60)], fill=COLOR_HEART_RED)
    # Brillo suave en el corazón
    draw.ellipse([hx - hr + 30, hy - hr + 40, hx - 40, hy - hr + 110], fill=(255, 140, 160, 150))
    
    # Brazos de Pooh rodeando el corazón
    draw.ellipse([cx - 350, cy + 180, cx - 110, cy + 390], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 110, cy + 180, cx + 350, cy + 390], fill=COLOR_POOH_GOLD)
    # Mangas
    draw.ellipse([cx - 340, cy + 160, cx - 210, cy + 290], fill=COLOR_SHIRT_RED)
    draw.ellipse([cx + 210, cy + 160, cx + 340, cy + 290], fill=COLOR_SHIRT_RED)
    
    # Cabeza tierna con mejillas rosas y ojos cerrados de amor
    draw_pooh_head(draw, cx, cy - 180, 270, eye_state="closed_happy", smile_type="warm")
    
    finalize_image(img, os.path.join(ASSETS_DIR, "pooh_hug.png"))

def gen_pooh_resting():
    """Pose 6: Sentado en el césped con una mariposa en la patita"""
    img = create_super_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_SIZE // 2, CANVAS_SIZE // 2 + 70
    
    # Pastito verde suave acuarela en la base
    draw.ellipse([cx - 480, cy + 620, cx + 480, cy + 770], fill=(165, 215, 140, 200))
    # Flores silvestres en el pasto
    for fx, fy in [(cx - 350, cy + 650), (cx + 360, cy + 660), (cx - 240, cy + 710)]:
        draw.ellipse([fx - 15, fy - 15, fx + 15, fy + 15], fill=(255, 255, 255, 220))
        draw.ellipse([fx - 6, fy - 6, fx + 6, fy + 6], fill=COLOR_HONEY_GOLD)
        
    # Patitas sentadas
    draw.ellipse([cx - 310, cy + 490, cx - 110, cy + 680], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 110, cy + 490, cx + 310, cy + 680], fill=COLOR_POOH_GOLD)
    
    # Cuerpo
    draw_pooh_body_base(draw, cx, cy + 240, 680, 690)
    
    # Brazo izquierdo apoyado en el suelo
    draw.ellipse([cx - 370, cy + 260, cx - 200, cy + 530], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx - 350, cy + 200, cx - 220, cy + 340], fill=COLOR_SHIRT_RED)
    
    # Brazo derecho extendido suavemente sosteniendo la mariposa
    draw.ellipse([cx + 140, cy + 120, cx + 370, cy + 320], fill=COLOR_POOH_GOLD)
    draw.ellipse([cx + 180, cy + 180, cx + 310, cy + 320], fill=COLOR_SHIRT_RED)
    
    # Mariposa azul cielo y violeta en la patita
    mx, my = cx + 380, cy + 110
    # Alas izquierdas
    draw.ellipse([mx - 70, my - 60, mx - 5, my + 10], fill=(120, 190, 255, 240))
    draw.ellipse([mx - 55, my, mx - 10, my + 45], fill=(180, 160, 255, 240))
    # Alas derechas
    draw.ellipse([mx + 5, my - 60, mx + 70, my + 10], fill=(120, 190, 255, 240))
    draw.ellipse([mx + 10, my, mx + 55, my + 45], fill=(180, 160, 255, 240))
    # Cuerpo de mariposa
    draw.ellipse([mx - 7, my - 25, mx + 7, my + 30], fill=COLOR_NOSE_BLACK)
    
    # Cabeza contemplando la mariposa con calma
    draw_pooh_head(draw, cx - 20, cy - 170, 270, eye_state="open", smile_type="peaceful")
    
    finalize_image(img, os.path.join(ASSETS_DIR, "pooh_resting.png"))

def gen_honey_pot_icon():
    """Tarrito de miel para la carta secreta y el ícono .ico"""
    img = create_super_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_SIZE // 2, CANVAS_SIZE // 2 + 50
    pw, ph = 1100, 1000
    
    # Sombra
    draw.ellipse([cx - 550, cy + ph // 2 - 20, cx + 550, cy + ph // 2 + 200], fill=(0, 0, 0, 30))
    
    # Tarro cerámico
    draw.rounded_rectangle([cx - pw // 2, cy - ph // 2, cx + pw // 2, cy + ph // 2], radius=160, fill=COLOR_HONEY_POT, outline=COLOR_HONEY_POT_DARK, width=int(SCALE * 7))
    # Tapa oscura
    draw.ellipse([cx - pw // 2 - 50, cy - ph // 2 - 100, cx + pw // 2 + 50, cy - ph // 2 + 130], fill=COLOR_HONEY_POT_DARK)
    # Miel desbordándose
    draw.ellipse([cx - pw // 2 - 20, cy - ph // 2 - 80, cx + pw // 2 + 20, cy - ph // 2 + 100], fill=COLOR_HONEY_GOLD)
    
    # Gotas gruesas de miel
    draw.rounded_rectangle([cx - 260, cy - ph // 2 + 50, cx - 110, cy - ph // 2 + 420], radius=65, fill=COLOR_HONEY_GOLD)
    draw.rounded_rectangle([cx + 120, cy - ph // 2 + 50, cx + 250, cy - ph // 2 + 320], radius=65, fill=COLOR_HONEY_GOLD)
    draw.rounded_rectangle([cx - 40, cy - ph // 2 + 50, cx + 50, cy - ph // 2 + 240], radius=40, fill=COLOR_HONEY_GOLD)
    
    # Etiqueta blanca de pergamino 'HUNNY'
    draw.rounded_rectangle([cx - 360, cy - 20, cx + 360, cy + 240], radius=50, fill=(255, 245, 220, 255), outline=COLOR_HONEY_POT_DARK, width=int(SCALE * 5))
    
    # Texto 'HUNNY' grande
    # H
    draw.line([(cx - 270, cy + 30), (cx - 270, cy + 190)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    draw.line([(cx - 190, cy + 30), (cx - 190, cy + 190)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    draw.line([(cx - 270, cy + 110), (cx - 190, cy + 110)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    # U
    draw.arc([cx - 140, cy + 30, cx - 40, cy + 190], 0, 180, fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    draw.line([(cx - 140, cy + 30), (cx - 140, cy + 110)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    draw.line([(cx - 40, cy + 30), (cx - 40, cy + 110)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    # N 1
    draw.line([(cx + 10, cy + 30), (cx + 10, cy + 190)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    draw.line([(cx + 10, cy + 30), (cx + 90, cy + 190)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    draw.line([(cx + 90, cy + 30), (cx + 90, cy + 190)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    # Y
    draw.line([(cx + 150, cy + 30), (cx + 200, cy + 110)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    draw.line([(cx + 250, cy + 30), (cx + 200, cy + 110)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    draw.line([(cx + 200, cy + 110), (cx + 200, cy + 190)], fill=COLOR_NOSE_BLACK, width=int(SCALE * 8))
    
    finalize_image(img, os.path.join(ASSETS_DIR, "honey_pot.png"))
    
    # Crear también el .ico multiresolución para Windows
    ico_img = img.resize((256, 256), Image.Resampling.LANCZOS)
    ico_img.save(os.path.join(ASSETS_DIR, "icon.ico"), format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])

if __name__ == "__main__":
    print("Generando ilustraciones de Winnie the Pooh...")
    gen_gift_closed()
    print("1/9 gift_closed.png OK")
    gen_gift_opened()
    print("2/9 gift_opened.png OK")
    gen_pooh_greeting()
    print("3/9 pooh_greeting.png OK")
    gen_pooh_thinking()
    print("4/9 pooh_thinking.png OK")
    gen_pooh_honey()
    print("5/9 pooh_honey.png OK")
    gen_pooh_balloon()
    print("6/9 pooh_balloon.png OK")
    gen_pooh_hug()
    print("7/9 pooh_hug.png OK")
    gen_pooh_resting()
    print("8/9 pooh_resting.png OK")
    gen_honey_pot_icon()
    print("9/9 honey_pot.png & icon.ico OK")
    print("¡Todas las ilustraciones generadas con éxito!")
