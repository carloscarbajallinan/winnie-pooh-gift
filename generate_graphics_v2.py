"""
generate_graphics_v2.py - Generador de Ilustraciones Clásicas 2D de Libro de Cuentos
Crea ilustraciones estilo acuarela con tinta de E.H. Shepard y Disney clásico:
1. 7 Personajes canónicos 2D: Pooh, Piglet, Igor, Tigger, Christopher Robin, Conejo, Búho.
2. 6 Escenarios icónicos de fondo del Bosque de los Cien Acres.
3. Textura de pergamino de carta antigua y libro abierto.
4. Caja de regalo misteriosa interactiva y tarrito de miel.
"""

import math
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSETS_DIR = r"C:\Users\LENOVO\.gemini\antigravity\scratch\winnie_pooh_gift\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

SCALE = 4
SIZE_CHAR = 512
CANVAS_CHAR = SIZE_CHAR * SCALE # 2048x2048

SIZE_BG_W = 860
SIZE_BG_H = 340
CANVAS_BG_W = SIZE_BG_W * 2
CANVAS_BG_H = SIZE_BG_H * 2

def get_char_canvas():
    return Image.new("RGBA", (CANVAS_CHAR, CANVAS_CHAR), (0, 0, 0, 0))

def save_char(img, filename):
    res = img.resize((SIZE_CHAR, SIZE_CHAR), Image.Resampling.LANCZOS)
    res.save(os.path.join(ASSETS_DIR, filename), "PNG")

def save_bg(img, filename):
    res = img.resize((SIZE_BG_W, SIZE_BG_H), Image.Resampling.LANCZOS)
    res.save(os.path.join(ASSETS_DIR, filename), "PNG")

# -------------------------------------------------------------
# ILUSTRACIONES 2D DE PERSONAJES (ESTILO CUENTO CLÁSICO)
# -------------------------------------------------------------

def gen_char_pooh():
    """Winnie the Pooh 2D clásico con estilo ilustración de libro"""
    img = get_char_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_CHAR // 2, CANVAS_CHAR // 2 + 60
    
    # Sombra acuarela en el suelo
    draw.ellipse([cx - 400, cy + 680, cx + 400, cy + 800], fill=(0, 0, 0, 30))
    
    # Colores estilo libro clásico (Acuarela Shepard/Disney)
    POOH_YELLOW = (248, 196, 68, 255)
    POOH_SHADOW = (220, 165, 45, 255)
    SHIRT_RED = (212, 45, 45, 255)
    INK_OUTLINE = (55, 38, 30, 255)
    
    # Patitas inferiores
    draw.ellipse([cx - 280, cy + 520, cx - 90, cy + 730], fill=POOH_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx + 90, cy + 520, cx + 280, cy + 730], fill=POOH_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    
    # Cuerpo redondo y barriguita de oso
    draw.ellipse([cx - 360, cy + 120, cx + 360, cy + 660], fill=POOH_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 4))
    
    # Camiseta roja corta clásica con arrugas de tela estilo dibujo a pluma
    draw.ellipse([cx - 370, cy + 80, cx + 370, cy + 420], fill=SHIRT_RED, outline=INK_OUTLINE, width=int(SCALE * 4))
    # Cuello de camiseta
    draw.arc([cx - 160, cy + 40, cx + 160, cy + 220], 10, 170, fill=INK_OUTLINE, width=int(SCALE * 4))
    
    # Tarro de miel en el brazo izquierdo
    pot_x, pot_y = cx - 250, cy + 450
    draw.rounded_rectangle([pot_x - 130, pot_y - 120, pot_x + 130, pot_y + 120], radius=40, fill=(180, 120, 70, 255), outline=INK_OUTLINE, width=int(SCALE * 3))
    draw.ellipse([pot_x - 140, pot_y - 140, pot_x + 140, pot_y - 80], fill=(245, 195, 30, 255), outline=INK_OUTLINE, width=int(SCALE * 3))
    # Etiqueta HUNNY
    draw.rounded_rectangle([pot_x - 80, pot_y - 20, pot_x + 80, pot_y + 50], radius=15, fill=(255, 248, 220, 255))
    draw.text((pot_x - 55, pot_y - 10), "HUNNY", fill=INK_OUTLINE, font=None)
    
    # Brazo izquierdo sosteniendo el tarro
    draw.ellipse([cx - 380, cy + 200, cx - 180, cy + 480], fill=POOH_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx - 380, cy + 150, cx - 240, cy + 320], fill=SHIRT_RED, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    
    # Brazo derecho saludando amablemente
    draw.ellipse([cx + 200, cy - 20, cx + 380, cy + 300], fill=POOH_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx + 240, cy - 100, cx + 390, cy + 60], fill=POOH_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx + 180, cy + 150, cx + 330, cy + 320], fill=SHIRT_RED, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    
    # Cabeza clásica redondeada
    head_y = cy - 200
    r = 280
    # Orejas
    draw.ellipse([cx - 240, head_y - 250, cx - 80, head_y - 90], fill=POOH_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx + 80, head_y - 250, cx + 240, head_y - 90], fill=POOH_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    # Cabeza
    draw.ellipse([cx - r, head_y - r * 0.85, cx + r, head_y + r * 0.95], fill=POOH_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 4))
    # Hocico
    draw.ellipse([cx - 160, head_y + 20, cx + 160, head_y + 220], fill=(255, 215, 110, 255), outline=INK_OUTLINE, width=int(SCALE * 3))
    # Nariz negra de botón
    draw.ellipse([cx - 60, head_y + 40, cx + 60, head_y + 110], fill=INK_OUTLINE)
    draw.ellipse([cx - 20, head_y + 50, cx + 10, head_y + 75], fill=(255, 255, 255, 180)) # Brillo
    # Ojos dulces con tinta
    draw.ellipse([cx - 110, head_y - 20, cx - 70, head_y + 25], fill=INK_OUTLINE)
    draw.ellipse([cx + 70, head_y - 20, cx + 110, head_y + 25], fill=INK_OUTLINE)
    # Cejitas de oso bueno
    draw.arc([cx - 130, head_y - 70, cx - 60, head_y - 30], 200, 340, fill=INK_OUTLINE, width=int(SCALE * 3))
    draw.arc([cx + 60, head_y - 70, cx + 130, head_y - 30], 200, 340, fill=INK_OUTLINE, width=int(SCALE * 3))
    # Sonrisa suave
    draw.arc([cx - 80, head_y + 100, cx + 80, head_y + 180], 20, 160, fill=INK_OUTLINE, width=int(SCALE * 3.5))
    
    save_char(img, "char_pooh.png")

def gen_char_piglet():
    """Piglet / Puerquito 2D con orejitas grandes y sueter a rayas rosa"""
    img = get_char_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_CHAR // 2, CANVAS_CHAR // 2 + 100
    
    INK_OUTLINE = (55, 38, 30, 255)
    PIGLET_PINK = (255, 195, 205, 255)
    SWEATER_DARK = (215, 120, 140, 255)
    
    # Sombra
    draw.ellipse([cx - 240, cy + 550, cx + 240, cy + 640], fill=(0, 0, 0, 30))
    
    # Patitas delgaditas de Piglet
    draw.ellipse([cx - 130, cy + 420, cx - 30, cy + 580], fill=PIGLET_PINK, outline=INK_OUTLINE, width=int(SCALE * 3))
    draw.ellipse([cx + 30, cy + 420, cx + 130, cy + 580], fill=PIGLET_PINK, outline=INK_OUTLINE, width=int(SCALE * 3))
    
    # Suéter rosa a rayas (cuerpo estilizado en forma de pera)
    sw_top, sw_bottom = cy + 60, cy + 460
    draw.ellipse([cx - 180, sw_top, cx + 180, sw_bottom], fill=PIGLET_PINK, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    # Rayas horizontales de sueter
    for ry in range(sw_top + 50, sw_bottom - 30, 60):
        draw.arc([cx - 170, ry - 30, cx + 170, ry + 40], 10, 170, fill=SWEATER_DARK, width=int(SCALE * 4))
        
    # Manitas tímidas juntas sosteniendo una flor
    draw.ellipse([cx - 120, cy + 180, cx - 20, cy + 320], fill=PIGLET_PINK, outline=INK_OUTLINE, width=int(SCALE * 3))
    draw.ellipse([cx + 20, cy + 180, cx + 120, cy + 320], fill=PIGLET_PINK, outline=INK_OUTLINE, width=int(SCALE * 3))
    # Flor silvestre
    draw.line([(cx, cy + 240), (cx, cy + 130)], fill=(70, 140, 60, 255), width=int(SCALE * 3))
    draw.ellipse([cx - 35, cy + 90, cx + 35, cy + 140], fill=(255, 230, 70, 255), outline=INK_OUTLINE, width=int(SCALE * 2))
    
    # Cabeza de Piglet
    hy = cy - 140
    # Grandes orejas puntiagudas rosas de Piglet
    draw.polygon([(cx - 180, hy - 400), (cx - 70, hy - 80), (cx - 240, hy - 30)], fill=PIGLET_PINK, outline=INK_OUTLINE)
    draw.polygon([(cx + 180, hy - 400), (cx + 70, hy - 80), (cx + 240, hy - 30)], fill=PIGLET_PINK, outline=INK_OUTLINE)
    # Cabeza redondita
    draw.ellipse([cx - 170, hy - 140, cx + 170, hy + 170], fill=PIGLET_PINK, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    # Hocico prominente de cerdito
    draw.ellipse([cx - 80, hy + 20, cx + 80, hy + 120], fill=(255, 160, 180, 255), outline=INK_OUTLINE, width=int(SCALE * 3))
    draw.ellipse([cx - 40, hy + 45, cx - 15, hy + 75], fill=INK_OUTLINE)
    draw.ellipse([cx + 15, hy + 45, cx + 40, hy + 75], fill=INK_OUTLINE)
    # Ojos tiernos
    draw.ellipse([cx - 75, hy - 40, cx - 45, hy - 5], fill=INK_OUTLINE)
    draw.ellipse([cx + 45, hy - 40, cx + 75, hy - 5], fill=INK_OUTLINE)
    # Sonrisa tímida
    draw.arc([cx - 50, hy + 80, cx + 50, hy + 140], 20, 160, fill=INK_OUTLINE, width=int(SCALE * 3))
    
    save_char(img, "char_piglet.png")

def gen_char_eeyore():
    """Igor (Eeyore) 2D con orejas caídas, lazo rosa en la cola y expresión melancólica dulce"""
    img = get_char_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_CHAR // 2, CANVAS_CHAR // 2 + 100
    
    INK_OUTLINE = (55, 38, 30, 255)
    EEYORE_GREY = (130, 145, 175, 255)
    EEYORE_SNOUT = (210, 190, 205, 255)
    
    # Sombra
    draw.ellipse([cx - 420, cy + 560, cx + 420, cy + 680], fill=(0, 0, 0, 30))
    
    # Cola a un lado con clavo y lazo rosa icónico
    draw.line([(cx + 300, cy + 350), (cx + 420, cy + 500)], fill=EEYORE_GREY, width=int(SCALE * 6))
    # Lazo rosa en la cola
    draw.ellipse([cx + 390, cy + 470, cx + 460, cy + 530], fill=(245, 110, 150, 255), outline=INK_OUTLINE, width=int(SCALE * 2.5))
    # Clavo plateado
    draw.ellipse([cx + 300, cy + 340, cx + 325, cy + 365], fill=(200, 200, 210, 255), outline=INK_OUTLINE, width=int(SCALE * 2))
    
    # Patitas sentadas
    draw.ellipse([cx - 320, cy + 380, cx - 120, cy + 600], fill=EEYORE_GREY, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx + 120, cy + 380, cx + 320, cy + 600], fill=EEYORE_GREY, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    
    # Cuerpo rechoncho
    draw.ellipse([cx - 300, cy + 100, cx + 300, cy + 550], fill=EEYORE_GREY, outline=INK_OUTLINE, width=int(SCALE * 4))
    
    # Melena negra corta en la espalda / cuello
    for my in range(cy - 120, cy + 150, 25):
        draw.line([(cx, my), (cx + 35, my - 15)], fill=INK_OUTLINE, width=int(SCALE * 3.5))
        
    # Cabeza inclinada de burrito
    hy = cy - 80
    # Grandes orejas largas y caídas
    draw.polygon([(cx - 150, hy - 60), (cx - 380, hy + 260), (cx - 260, hy + 300)], fill=EEYORE_GREY, outline=INK_OUTLINE)
    draw.polygon([(cx + 150, hy - 60), (cx + 380, hy + 260), (cx + 260, hy + 300)], fill=EEYORE_GREY, outline=INK_OUTLINE)
    
    # Cabeza alargada
    draw.ellipse([cx - 210, hy - 160, cx + 210, hy + 180], fill=EEYORE_GREY, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    # Hocico alargado rosáceo
    draw.ellipse([cx - 150, hy + 30, cx + 150, hy + 230], fill=EEYORE_SNOUT, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    # Costura característica en la nariz
    draw.line([(cx, hy + 50), (cx, hy + 200)], fill=INK_OUTLINE, width=int(SCALE * 2.5))
    for sy in range(hy + 80, hy + 190, 30):
        draw.line([(cx - 15, sy), (cx + 15, sy)], fill=INK_OUTLINE, width=int(SCALE * 2))
    # Ojos caídos pensativos
    draw.ellipse([cx - 100, hy - 40, cx - 60, hy], fill=INK_OUTLINE)
    draw.ellipse([cx + 60, hy - 40, cx + 100, hy], fill=INK_OUTLINE)
    # Cejas inclinadas de nostalgia
    draw.line([(cx - 110, hy - 70), (cx - 50, hy - 50)], fill=INK_OUTLINE, width=int(SCALE * 3))
    draw.line([(cx + 110, hy - 70), (cx + 50, hy - 50)], fill=INK_OUTLINE, width=int(SCALE * 3))
    
    save_char(img, "char_eeyore.png")

def gen_char_tigger():
    """Tigger 2D sobre su cola con rayas negras, hocico amarillo y sonrisa saltarina"""
    img = get_char_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_CHAR // 2, CANVAS_CHAR // 2 + 50
    
    INK_OUTLINE = (55, 38, 30, 255)
    TIGGER_ORANGE = (245, 130, 45, 255)
    TIGGER_YELLOW = (255, 220, 115, 255)
    
    # Cola en forma de resorte espiral rebotando
    draw.arc([cx - 140, cy + 420, cx + 140, cy + 680], 40, 320, fill=TIGGER_ORANGE, width=int(SCALE * 7))
    draw.arc([cx - 100, cy + 540, cx + 100, cy + 780], 40, 320, fill=TIGGER_ORANGE, width=int(SCALE * 7))
    
    # Rayas en la cola
    for ry in [cy + 480, cy + 560, cy + 640]:
        draw.line([(cx - 40, ry), (cx + 40, ry)], fill=INK_OUTLINE, width=int(SCALE * 4))
        
    # Cuerpo esbelto y alegre
    draw.ellipse([cx - 220, cy + 120, cx + 220, cy + 500], fill=TIGGER_ORANGE, outline=INK_OUTLINE, width=int(SCALE * 4))
    # Barriguita amarilla
    draw.ellipse([cx - 120, cy + 160, cx + 120, cy + 460], fill=TIGGER_YELLOW)
    
    # Rayas de tigre en los costados
    for sy in range(cy + 180, cy + 440, 60):
        draw.polygon([(cx - 210, sy), (cx - 120, sy + 15), (cx - 200, sy + 30)], fill=INK_OUTLINE)
        draw.polygon([(cx + 210, sy), (cx + 120, sy + 15), (cx + 200, sy + 30)], fill=INK_OUTLINE)
        
    # Brazos abiertos enérgicos
    draw.ellipse([cx - 380, cy + 100, cx - 180, cy + 280], fill=TIGGER_ORANGE, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx + 180, cy + 100, cx + 380, cy + 280], fill=TIGGER_ORANGE, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    
    # Cabeza de Tigger
    hy = cy - 140
    # Orejitas redondas
    draw.ellipse([cx - 200, hy - 200, cx - 90, hy - 90], fill=TIGGER_ORANGE, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx + 90, hy - 200, cx + 200, hy - 90], fill=TIGGER_ORANGE, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    
    # Cabeza alargada
    draw.ellipse([cx - 180, hy - 140, cx + 180, hy + 160], fill=TIGGER_ORANGE, outline=INK_OUTLINE, width=int(SCALE * 4))
    # Barbilla / hocico grande amarillo
    draw.ellipse([cx - 140, hy, cx + 140, hy + 200], fill=TIGGER_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    # Nariz rosada de gato
    draw.ellipse([cx - 45, hy + 20, cx + 45, hy + 75], fill=(235, 95, 115, 255), outline=INK_OUTLINE, width=int(SCALE * 2.5))
    # Bigotes
    draw.line([(cx - 80, hy + 70), (cx - 180, hy + 60)], fill=INK_OUTLINE, width=int(SCALE * 2.5))
    draw.line([(cx - 80, hy + 90), (cx - 170, hy + 100)], fill=INK_OUTLINE, width=int(SCALE * 2.5))
    draw.line([(cx + 80, hy + 70), (cx + 180, hy + 60)], fill=INK_OUTLINE, width=int(SCALE * 2.5))
    draw.line([(cx + 80, hy + 90), (cx + 170, hy + 100)], fill=INK_OUTLINE, width=int(SCALE * 2.5))
    # Ojos picaros
    draw.ellipse([cx - 70, hy - 50, cx - 35, hy - 15], fill=INK_OUTLINE)
    draw.ellipse([cx + 35, hy - 50, cx + 70, hy - 15], fill=INK_OUTLINE)
    # Gran sonrisa saltarina
    draw.arc([cx - 90, hy + 90, cx + 90, hy + 180], 20, 160, fill=INK_OUTLINE, width=int(SCALE * 3.5))
    
    save_char(img, "char_tigger.png")

def gen_char_christopher():
    """Christopher Robin 2D con polo amarillo, shorts azules y botas"""
    img = get_char_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_CHAR // 2, CANVAS_CHAR // 2 + 50
    
    INK_OUTLINE = (55, 38, 30, 255)
    SHIRT_YELLOW = (255, 230, 110, 255)
    PANTS_BLUE = (80, 130, 185, 255)
    SKIN_PEACH = (255, 222, 195, 255)
    HAIR_BROWN = (145, 90, 50, 255)
    
    # Sombra
    draw.ellipse([cx - 280, cy + 620, cx + 280, cy + 720], fill=(0, 0, 0, 30))
    
    # Piernas y botas
    draw.rounded_rectangle([cx - 120, cy + 340, cx - 40, cy + 550], radius=20, fill=SKIN_PEACH, outline=INK_OUTLINE, width=int(SCALE * 3))
    draw.rounded_rectangle([cx + 40, cy + 340, cx + 120, cy + 550], radius=20, fill=SKIN_PEACH, outline=INK_OUTLINE, width=int(SCALE * 3))
    # Botas marrones
    draw.ellipse([cx - 140, cy + 520, cx - 20, cy + 660], fill=(130, 75, 45, 255), outline=INK_OUTLINE, width=int(SCALE * 3))
    draw.ellipse([cx + 20, cy + 520, cx + 140, cy + 660], fill=(130, 75, 45, 255), outline=INK_OUTLINE, width=int(SCALE * 3))
    
    # Shorts azules
    draw.rounded_rectangle([cx - 160, cy + 220, cx + 160, cy + 380], radius=30, fill=PANTS_BLUE, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    
    # Polo amarillo con cuello blanco
    draw.ellipse([cx - 200, cy - 20, cx + 200, cy + 260], fill=SHIRT_YELLOW, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    # Cuellito blanco de camisa
    draw.polygon([(cx - 70, cy), (cx, cy + 50), (cx - 10, cy - 20)], fill=(255, 255, 255, 255), outline=INK_OUTLINE)
    draw.polygon([(cx + 70, cy), (cx, cy + 50), (cx + 10, cy - 20)], fill=(255, 255, 255, 255), outline=INK_OUTLINE)
    
    # Brazos amables
    draw.ellipse([cx - 280, cy + 40, cx - 140, cy + 280], fill=SKIN_PEACH, outline=INK_OUTLINE, width=int(SCALE * 3))
    draw.ellipse([cx + 140, cy + 40, cx + 280, cy + 280], fill=SKIN_PEACH, outline=INK_OUTLINE, width=int(SCALE * 3))
    
    # Cabeza y cabello
    hy = cy - 160
    draw.ellipse([cx - 160, hy - 140, cx + 160, hy + 160], fill=SKIN_PEACH, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    # Cabello castaño clásico estilo años 20
    draw.ellipse([cx - 180, hy - 190, cx + 180, hy + 10], fill=HAIR_BROWN, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.arc([cx - 170, hy - 80, cx - 80, hy + 50], 120, 300, fill=HAIR_BROWN, width=int(SCALE * 5))
    # Ojos y sonrisa dulce y protectora
    draw.ellipse([cx - 80, hy - 20, cx - 50, hy + 15], fill=INK_OUTLINE)
    draw.ellipse([cx + 50, hy - 20, cx + 80, hy + 15], fill=INK_OUTLINE)
    draw.arc([cx - 60, hy + 60, cx + 60, hy + 120], 20, 160, fill=INK_OUTLINE, width=int(SCALE * 3))
    
    save_char(img, "char_christopher.png")

def gen_char_rabbit():
    """Conejo (Rabbit) 2D con orejas largas y una zanahoria"""
    img = get_char_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_CHAR // 2, CANVAS_CHAR // 2 + 70
    
    INK_OUTLINE = (55, 38, 30, 255)
    RABBIT_CREAM = (248, 235, 185, 255)
    
    # Sombra
    draw.ellipse([cx - 280, cy + 580, cx + 280, cy + 680], fill=(0, 0, 0, 30))
    # Patas largas
    draw.ellipse([cx - 220, cy + 460, cx - 60, cy + 620], fill=RABBIT_CREAM, outline=INK_OUTLINE, width=int(SCALE * 3))
    draw.ellipse([cx + 60, cy + 460, cx + 220, cy + 620], fill=RABBIT_CREAM, outline=INK_OUTLINE, width=int(SCALE * 3))
    # Cuerpo
    draw.ellipse([cx - 200, cy + 140, cx + 200, cy + 520], fill=RABBIT_CREAM, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    
    # Zanahoria en sus manitas
    zx, zy = cx, cy + 240
    draw.polygon([(zx - 30, zy - 40), (zx + 30, zy - 40), (zx, zy + 120)], fill=(245, 120, 35, 255), outline=INK_OUTLINE)
    draw.line([(zx, zy - 40), (zx - 20, zy - 90)], fill=(70, 160, 50, 255), width=int(SCALE * 3))
    draw.line([(zx, zy - 40), (zx + 20, zy - 90)], fill=(70, 160, 50, 255), width=int(SCALE * 3))
    
    # Cabeza y orejas largas
    hy = cy - 120
    # Orejas
    draw.ellipse([cx - 140, hy - 440, cx - 40, hy - 60], fill=RABBIT_CREAM, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx + 40, hy - 440, cx + 140, hy - 60], fill=RABBIT_CREAM, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    # Cabeza
    draw.ellipse([cx - 160, hy - 120, cx + 160, hy + 140], fill=RABBIT_CREAM, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    # Ojos y bigotes
    draw.ellipse([cx - 70, hy - 40, cx - 40, hy - 10], fill=INK_OUTLINE)
    draw.ellipse([cx + 40, hy - 40, cx + 70, hy - 10], fill=INK_OUTLINE)
    draw.polygon([(cx - 25, hy + 20), (cx + 25, hy + 20), (cx, hy + 45)], fill=(245, 140, 160, 255), outline=INK_OUTLINE)
    
    save_char(img, "char_rabbit.png")

def gen_char_owl():
    """Búho (Owl) 2D con plumas sabias y aspecto académico de cuento"""
    img = get_char_canvas()
    draw = ImageDraw.Draw(img)
    cx, cy = CANVAS_CHAR // 2, CANVAS_CHAR // 2 + 50
    
    INK_OUTLINE = (55, 38, 30, 255)
    OWL_BROWN = (175, 125, 80, 255)
    OWL_BEIGE = (245, 230, 190, 255)
    
    # Tronco de árbol donde se posa
    draw.rounded_rectangle([cx - 380, cy + 450, cx + 380, cy + 620], radius=30, fill=(115, 75, 45, 255), outline=INK_OUTLINE, width=int(SCALE * 3.5))
    
    # Patitas con garras sobre la rama
    for px in [cx - 120, cx - 80, cx - 40, cx + 40, cx + 80, cx + 120]:
        draw.line([(px, cy + 420), (px, cy + 470)], fill=(240, 180, 40, 255), width=int(SCALE * 4))
        
    # Cuerpo y alas
    draw.ellipse([cx - 260, cy - 20, cx + 260, cy + 460], fill=OWL_BROWN, outline=INK_OUTLINE, width=int(SCALE * 4))
    draw.ellipse([cx - 150, cy + 80, cx + 150, cy + 420], fill=OWL_BEIGE)
    
    # Cabeza con penachos de plumas
    hy = cy - 140
    draw.polygon([(cx - 220, hy - 160), (cx - 120, hy - 40), (cx - 240, hy + 20)], fill=OWL_BROWN, outline=INK_OUTLINE)
    draw.polygon([(cx + 220, hy - 160), (cx + 120, hy - 40), (cx + 240, hy + 20)], fill=OWL_BROWN, outline=INK_OUTLINE)
    draw.ellipse([cx - 220, hy - 100, cx + 220, hy + 160], fill=OWL_BROWN, outline=INK_OUTLINE, width=int(SCALE * 3.5))
    
    # Ojos redondos sabios con anteojos
    draw.ellipse([cx - 130, hy - 50, cx - 20, hy + 60], fill=(255, 245, 200, 255), outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx + 20, hy - 50, cx + 130, hy + 60], fill=(255, 245, 200, 255), outline=INK_OUTLINE, width=int(SCALE * 3.5))
    draw.ellipse([cx - 85, hy - 15, cx - 55, hy + 25], fill=INK_OUTLINE)
    draw.ellipse([cx + 55, hy - 15, cx + 85, hy + 25], fill=INK_OUTLINE)
    # Pico
    draw.polygon([(cx - 25, hy + 30), (cx + 25, hy + 30), (cx, hy + 85)], fill=(240, 160, 40, 255), outline=INK_OUTLINE)
    
    save_char(img, "char_owl.png")

# -------------------------------------------------------------
# ESCENARIOS DE FONDO DEL BOSQUE (ACUARELA SUAVE DE LIBRO)
# -------------------------------------------------------------

def gen_bg_pooh_house():
    """1. La Casa del Árbol de Pooh con letrero 'Mr Sanders'"""
    img = Image.new("RGBA", (CANVAS_BG_W, CANVAS_BG_H), (245, 248, 235, 255))
    draw = ImageDraw.Draw(img)
    w, h = CANVAS_BG_W, CANVAS_BG_H
    
    # Cielo acuarela dorado y menta
    draw.rectangle([0, 0, w, h // 2], fill=(240, 246, 230, 255))
    
    # Colinas verdes suaves
    draw.ellipse([-200, h - 350, w // 2 + 100, h + 300], fill=(185, 220, 155, 255))
    draw.ellipse([w // 2 - 100, h - 380, w + 300, h + 300], fill=(165, 205, 135, 255))
    
    # Gran tronco del roble de Pooh en el centro-derecha
    tree_x = w // 2 + 150
    draw.rectangle([tree_x - 220, 0, tree_x + 220, h], fill=(145, 105, 65, 255))
    # Hojas superiores del árbol
    draw.ellipse([tree_x - 450, -200, tree_x + 450, 250], fill=(120, 175, 90, 240))
    
    # Puerta redonda de madera en el tronco
    door_y = h - 220
    draw.ellipse([tree_x - 110, door_y - 120, tree_x + 110, door_y + 120], fill=(110, 70, 40, 255))
    draw.ellipse([tree_x - 90, door_y - 100, tree_x + 90, door_y + 100], fill=(130, 85, 50, 255))
    # Pomo de la puerta
    draw.ellipse([tree_x + 45, door_y - 10, tree_x + 75, door_y + 20], fill=(240, 195, 60, 255))
    
    # Letrero rústico 'Mr Sanders' sobre la puerta
    sign_y = door_y - 170
    draw.rounded_rectangle([tree_x - 130, sign_y - 45, tree_x + 130, sign_y + 45], radius=15, fill=(245, 235, 205, 255), outline=(90, 60, 35, 255), width=4)
    # Pequeño tejado de paja/madera sobre la puerta
    draw.polygon([(tree_x - 160, sign_y - 50), (tree_x + 160, sign_y - 50), (tree_x, sign_y - 100)], fill=(75, 125, 60, 255))
    
    save_bg(img, "bg_pooh_house.png")

def gen_bg_bridge():
    """2. El Puente de los Palitos (Poohsticks Bridge) sobre el río"""
    img = Image.new("RGBA", (CANVAS_BG_W, CANVAS_BG_H), (235, 245, 250, 255))
    draw = ImageDraw.Draw(img)
    w, h = CANVAS_BG_W, CANVAS_BG_H
    
    # Río azul acuarela cristalino abajo
    draw.rectangle([0, h // 2, w, h], fill=(160, 215, 235, 255))
    # Ondas y nenúfares
    for oy in range(h // 2 + 50, h, 60):
        draw.line([(0, oy), (w, oy)], fill=(140, 195, 220, 180), width=3)
    # Nenúfares verdes
    for nx, ny in [(200, h - 80), (600, h - 120), (1200, h - 90)]:
        draw.ellipse([nx - 45, ny - 20, nx + 45, ny + 20], fill=(100, 180, 110, 255))
        draw.ellipse([nx, ny - 15, nx + 25, ny + 5], fill=(255, 235, 245, 255)) # Flor
        
    # Árboles ribereños en las orillas
    draw.ellipse([-100, 50, 400, h // 2 + 50], fill=(130, 190, 115, 255))
    draw.ellipse([w - 400, 50, w + 100, h // 2 + 50], fill=(145, 200, 125, 255))
    
    # Puente de madera rústica atravesando
    by = h // 2 - 40
    draw.rectangle([0, by, w, by + 50], fill=(140, 100, 65, 255))
    # Barandilla rústica de troncos
    draw.line([(0, by - 55), (w, by - 55)], fill=(120, 80, 50, 255), width=10)
    for px in range(80, w, 160):
        draw.line([(px, by - 70), (px, by + 50)], fill=(110, 70, 40, 255), width=8)
        
    save_bg(img, "bg_bridge.png")

def gen_bg_gloomy_place():
    """3. El Rincón de Igor con su casita de ramas y cardos"""
    img = Image.new("RGBA", (CANVAS_BG_W, CANVAS_BG_H), (235, 238, 245, 255))
    draw = ImageDraw.Draw(img)
    w, h = CANVAS_BG_W, CANVAS_BG_H
    
    # Nubes suaves de acuarela
    draw.ellipse([200, 30, 700, 180], fill=(220, 225, 235, 200))
    draw.ellipse([900, 50, 1400, 200], fill=(215, 220, 230, 200))
    
    # Colina suave melancólica
    draw.ellipse([-100, h - 300, w + 100, h + 300], fill=(175, 195, 170, 255))
    
    # Casita de ramas cruzadas de Igor a la derecha
    hx, hy = w // 2 + 250, h - 160
    for ang in [-40, -20, 0, 20, 40]:
        rad = math.radians(ang)
        x2 = hx + math.sin(rad) * 140
        y2 = hy - math.cos(rad) * 140
        draw.line([(hx, hy + 60), (x2, y2)], fill=(110, 80, 55, 255), width=8)
        
    # Cardos púrpuras silvestres (la comida favorita de Igor)
    for cx in [150, 320, w - 200]:
        draw.line([(cx, h - 60), (cx, h - 130)], fill=(90, 140, 85, 255), width=6)
        draw.ellipse([cx - 25, h - 170, cx + 25, h - 120], fill=(175, 125, 195, 255)) # Flor púrpura
        
    save_bg(img, "bg_gloomy_place.png")

def gen_bg_bee_tree():
    """4. El Gran Roble de la Miel con abejitas y tarros"""
    img = Image.new("RGBA", (CANVAS_BG_W, CANVAS_BG_H), (255, 250, 230, 255))
    draw = ImageDraw.Draw(img)
    w, h = CANVAS_BG_W, CANVAS_BG_H
    
    # Prado soleado
    draw.ellipse([-200, h - 280, w + 200, h + 300], fill=(195, 225, 135, 255))
    
    # Tronco del roble sagrado con hueco de colmena
    tree_x = w // 2 - 180
    draw.rectangle([tree_x - 180, 0, tree_x + 180, h], fill=(135, 95, 55, 255))
    # Follaje
    draw.ellipse([tree_x - 380, -180, tree_x + 380, 220], fill=(115, 180, 80, 230))
    # Hueco del nudo de miel
    hole_y = 180
    draw.ellipse([tree_x - 60, hole_y - 70, tree_x + 60, hole_y + 70], fill=(65, 40, 20, 255))
    # Miel dorada desbordándose del hueco
    draw.rounded_rectangle([tree_x - 30, hole_y, tree_x + 30, hole_y + 110], radius=15, fill=(255, 205, 40, 255))
    
    # Abejitas zumbando alrededor
    bees = [(tree_x + 140, hole_y - 40), (tree_x - 120, hole_y + 60), (tree_x + 90, hole_y + 100)]
    for bx, by in bees:
        draw.ellipse([bx - 16, by - 10, bx + 16, by + 10], fill=(255, 210, 45, 255))
        draw.line([(bx - 5, by - 10), (bx - 5, by + 10)], fill=(45, 30, 20, 255), width=3)
        draw.line([(bx + 5, by - 10), (bx + 5, by + 10)], fill=(45, 30, 20, 255), width=3)
        # Alitas
        draw.ellipse([bx - 10, by - 24, bx + 10, by - 5], fill=(255, 255, 255, 190))
        
    save_bg(img, "bg_bee_tree.png")

def gen_bg_rabbit_garden():
    """5. El Jardín de Conejo con cercas rústicas y zanahorias"""
    img = Image.new("RGBA", (CANVAS_BG_W, CANVAS_BG_H), (245, 248, 235, 255))
    draw = ImageDraw.Draw(img)
    w, h = CANVAS_BG_W, CANVAS_BG_H
    
    # Huerto con hileras de tierra fértil
    draw.rectangle([0, h // 2 - 20, w, h], fill=(190, 220, 145, 255))
    # Hileras de cultivo
    for ry in range(h // 2 + 50, h, 60):
        draw.ellipse([-50, ry, w + 50, ry + 40], fill=(130, 95, 65, 255))
        # Hojas de zanahorias asomando
        for zx in range(120, w - 100, 140):
            draw.line([(zx, ry + 15), (zx - 15, ry - 20)], fill=(70, 160, 60, 255), width=5)
            draw.line([(zx, ry + 15), (zx + 15, ry - 20)], fill=(70, 160, 60, 255), width=5)
            
    # Cerca blanca de madera rústica
    fy = h // 2 - 60
    draw.line([(0, fy + 20), (w, fy + 20)], fill=(245, 240, 230, 255), width=12)
    draw.line([(0, fy + 55), (w, fy + 55)], fill=(245, 240, 230, 255), width=12)
    for px in range(60, w, 110):
        draw.polygon([(px - 14, fy + 80), (px + 14, fy + 80), (px + 14, fy), (px, fy - 18), (px - 14, fy)], fill=(255, 252, 245, 255), outline=(190, 180, 165, 255), width=2)
        
    save_bg(img, "bg_rabbit_garden.png")

def gen_bg_galleons_lap():
    """6. La Colina de Christopher Robin al atardecer"""
    img = Image.new("RGBA", (CANVAS_BG_W, CANVAS_BG_H), (255, 230, 215, 255))
    draw = ImageDraw.Draw(img)
    w, h = CANVAS_BG_W, CANVAS_BG_H
    
    # Cielo atardecer durazno / lila
    draw.rectangle([0, 0, w, h // 2], fill=(255, 220, 205, 255))
    # Sol suave dorado
    draw.ellipse([w // 2 + 200, 50, w // 2 + 380, 230], fill=(255, 235, 160, 220))
    
    # Cima de la colina encantada
    draw.ellipse([-200, h - 340, w + 200, h + 300], fill=(175, 215, 145, 255))
    
    # Árbol solitario icónico en la cima
    tx = w // 2 - 250
    draw.line([(tx, h - 140), (tx, h - 280)], fill=(105, 70, 45, 255), width=24)
    draw.ellipse([tx - 180, h - 480, tx + 180, h - 240], fill=(110, 165, 95, 240))
    
    save_bg(img, "bg_galleons_lap.png")

if __name__ == "__main__":
    print("Generando personajes 2D clásicos de cuento...")
    gen_char_pooh()
    gen_char_piglet()
    gen_char_eeyore()
    gen_char_tigger()
    gen_char_christopher()
    gen_char_rabbit()
    gen_char_owl()
    print("Personajes 2D OK")
    
    print("Generando escenarios de fondo...")
    gen_bg_pooh_house()
    gen_bg_bridge()
    gen_bg_gloomy_place()
    gen_bg_bee_tree()
    gen_bg_rabbit_garden()
    gen_bg_galleons_lap()
    print("Escenarios OK")
