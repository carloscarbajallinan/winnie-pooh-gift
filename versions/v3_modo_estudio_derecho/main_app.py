"""
main_app.py - Winnie the Pooh: El Libro Ilustrado del Bosque de los Cien Acres
Edición especial de regalo con ilustraciones 2D auténticas, cambios de pose
reactivos (5+ poses por personaje), 6 escenarios intercambiables,
selector de 3 pistas de música instrumental y MODO ESTUDIO DE DERECHO (Perú).
"""

import os
import sys
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Soporte para PyInstaller (--onefile)
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), relative_path)

# Motor de audio dual: Pygame Mixer (alto volumen) + Winsound (nativo Windows)
try:
    import pygame
    pygame.mixer.pre_init(44100, -16, 2, 1024)
    pygame.mixer.init()
    PYGAME_AUDIO_OK = True
except Exception:
    PYGAME_AUDIO_OK = False

try:
    import winsound
    WINSOUND_OK = True
except Exception:
    WINSOUND_OK = False

import wisdom_engine

# Colores y estilo de libro de cuentos antiguo
COLOR_PARCHMENT = "#FFFDF6"    # Fondo marfil cálido de página de libro
COLOR_BOOK_BORDER = "#E8D8BA"  # Costura / borde de página envejecida
COLOR_TEXT_INK = "#3C2E25"     # Tinta sepia / marrón oscuro clásico
COLOR_ACCENT_RED = "#C83232"   # Rojo amapola clásico
COLOR_ACCENT_GOLD = "#E8A725"  # Dorado miel
COLOR_BANNER_BG = "#FFF6E0"    # Cinta de capítulo
FONT_STORY_TITLE = ("Georgia", 15, "bold")
FONT_CHAPTER = ("Georgia", 11, "italic")
FONT_HANDWRITING = ("Georgia", 12, "italic")
FONT_BUTTON = ("Segoe UI", 9, "bold")

TRACKS = [
    ("music_theme1.wav", "Caja de Música Clásica 🎵"),
    ("music_theme2.wav", "Lofi Piano de Estudio ☕"),
    ("music_theme3.wav", "Campanillas Celestes 🍃")
]

class WinniePoohStorybookApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Winnie the Pooh & Sus Amigos — El Libro del Bosque de los Cien Acres 🍯")
        self.geometry("980x810")
        self.minsize(940, 750)
        self.configure(bg=COLOR_PARCHMENT)
        self.center_window(980, 810)
        
        icon_path = get_resource_path(os.path.join("assets", "icon.ico"))
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass
                
        # Estado
        self.current_state = "GIFT"
        self.music_enabled = True
        self.current_track_idx = 0
        self.study_mode_active = False
        self.current_char_id = "pooh"
        self.current_scenario_id = "pooh_house"
        self.char_pose_indices = {cid: 0 for cid in wisdom_engine.CHARACTERS_DATA.keys()}
        self.typewriter_job = None
        self.bg_music_channel = None
        
        # Cargar recursos (Poses auténticas 2D, fondos y audios)
        self.load_all_assets()
        
        # Iniciar música de fondo
        self.start_background_music()
        
        # Contenedor raíz
        self.root_frame = tk.Frame(self, bg=COLOR_PARCHMENT)
        self.root_frame.pack(fill="both", expand=True)
        
        # Iniciar en pantalla del regalo
        self.show_gift_cover()

    def center_window(self, width, height):
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - width) // 2
        y = (sh - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

    # =========================================================================
    # GESTIÓN DE AUDIO ROBUSTA CON CAMBIO DE PISTAS (ALTO VOLUMEN)
    # =========================================================================
    def start_background_music(self):
        if not self.music_enabled:
            return
        track_filename, _ = TRACKS[self.current_track_idx]
        theme_path = get_resource_path(os.path.join("assets", track_filename))
        
        if PYGAME_AUDIO_OK and os.path.exists(theme_path):
            try:
                if self.bg_music_channel:
                    self.bg_music_channel.stop()
                self.music_sound = pygame.mixer.Sound(theme_path)
                self.music_sound.set_volume(0.85)
                self.bg_music_channel = pygame.mixer.Channel(0)
                self.bg_music_channel.play(self.music_sound, loops=-1)
                return
            except Exception as e:
                print(f"Error pygame música: {e}")
                
        if WINSOUND_OK and os.path.exists(theme_path):
            try:
                winsound.PlaySound(theme_path, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            except Exception:
                pass

    def cycle_music_track(self):
        """Cambia entre las 3 pistas instrumentales relajantes"""
        self.current_track_idx = (self.current_track_idx + 1) % len(TRACKS)
        self.play_sound_effect("pop.wav")
        if self.music_enabled:
            self.start_background_music()
        self.update_music_buttons()

    def toggle_music(self):
        self.music_enabled = not self.music_enabled
        if self.music_enabled:
            self.start_background_music()
        else:
            if PYGAME_AUDIO_OK and self.bg_music_channel:
                self.bg_music_channel.stop()
            if WINSOUND_OK:
                winsound.PlaySound(None, winsound.SND_PURGE)
        self.update_music_buttons()

    def update_music_buttons(self):
        _, track_name = TRACKS[self.current_track_idx]
        if hasattr(self, 'btn_cycle_track'):
            self.btn_cycle_track.config(text=f"🎶 {track_name}")
        if hasattr(self, 'btn_music_toggle'):
            if self.music_enabled:
                self.btn_music_toggle.config(text="🔊 Sonando", bg="#FFEFC8")
            else:
                self.btn_music_toggle.config(text="🔇 Silencio", bg="#EAD8BA")

    def play_sound_effect(self, sound_filename):
        if not self.music_enabled:
            return
        sound_path = get_resource_path(os.path.join("assets", sound_filename))
        if not os.path.exists(sound_path):
            return
            
        if PYGAME_AUDIO_OK:
            try:
                snd = pygame.mixer.Sound(sound_path)
                snd.set_volume(0.95)
                pygame.mixer.Channel(1).play(snd)
                return
            except Exception:
                pass
                
        if WINSOUND_OK:
            try:
                winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception:
                pass

    # =========================================================================
    # CARGA DE ASSETS
    # =========================================================================
    def load_all_assets(self):
        assets_dir = get_resource_path("assets")
        poses_dir = os.path.join(assets_dir, "poses")
        
        self.img_gift_closed = ImageTk.PhotoImage(Image.open(os.path.join(assets_dir, "gift_closed.png")).resize((350, 350), Image.Resampling.LANCZOS))
        self.img_gift_opened = ImageTk.PhotoImage(Image.open(os.path.join(assets_dir, "gift_opened.png")).resize((350, 350), Image.Resampling.LANCZOS))
        self.img_honey_pot = ImageTk.PhotoImage(Image.open(os.path.join(assets_dir, "honey_pot.png")).resize((32, 32), Image.Resampling.LANCZOS))
        
        self.character_poses = {}
        for cid, poses_meta in wisdom_engine.CHARACTER_POSES.items():
            self.character_poses[cid] = []
            for p_info in poses_meta:
                p1 = os.path.join(poses_dir, p_info["file"])
                p2 = os.path.join(assets_dir, p_info["file"])
                p = p1 if os.path.exists(p1) else p2
                
                if os.path.exists(p):
                    img = Image.open(p).resize((320, 320), Image.Resampling.LANCZOS)
                    self.character_poses[cid].append((ImageTk.PhotoImage(img), p_info["caption"]))
                    
        self.scenario_images = {}
        for sid, sdata in wisdom_engine.SCENARIOS_DATA.items():
            p = os.path.join(assets_dir, sdata["file"])
            if os.path.exists(p):
                img = Image.open(p).resize((430, 170), Image.Resampling.LANCZOS)
                self.scenario_images[sid] = ImageTk.PhotoImage(img)

    # =========================================================================
    # PANTALLA 1: EL REGALO MISTERIOSO CON LAZO
    # =========================================================================
    def show_gift_cover(self):
        self.clear_frame()
        
        top_bar = tk.Frame(self.root_frame, bg=COLOR_PARCHMENT)
        top_bar.pack(fill="x", padx=20, pady=10)
        
        self.btn_cycle_track = tk.Button(
            top_bar, text=f"🎶 {TRACKS[self.current_track_idx][1]}", font=FONT_BUTTON,
            bg="#FFECC0", fg=COLOR_TEXT_INK, activebackground="#FFDF9B",
            relief="flat", cursor="hand2", padx=10, pady=5, command=self.cycle_music_track
        )
        self.btn_cycle_track.pack(side="right", padx=(6, 0))
        
        self.btn_music_toggle = tk.Button(
            top_bar, text="🔊 Sonando", font=FONT_BUTTON,
            bg="#FFEFC8", fg=COLOR_TEXT_INK, activebackground="#FFDF9B",
            relief="flat", cursor="hand2", padx=10, pady=5, command=self.toggle_music
        )
        self.btn_music_toggle.pack(side="right")
        
        center_frame = tk.Frame(self.root_frame, bg=COLOR_PARCHMENT)
        center_frame.pack(expand=True)
        
        title_lbl = tk.Label(
            center_frame,
            text="Un Paquete Especial para Alguien Inolvidable...",
            font=("Georgia", 19, "italic"),
            bg=COLOR_PARCHMENT,
            fg=COLOR_TEXT_INK
        )
        title_lbl.pack(pady=(0, 6))
        
        sub_lbl = tk.Label(
            center_frame,
            text="Enviado con cariño desde el corazón del Bosque de los Cien Acres 🍯",
            font=FONT_CHAPTER,
            bg=COLOR_PARCHMENT,
            fg="#826E5D"
        )
        sub_lbl.pack(pady=(0, 15))
        
        self.gift_lbl = tk.Label(
            center_frame,
            image=self.img_gift_closed,
            bg=COLOR_PARCHMENT,
            cursor="hand2"
        )
        self.gift_lbl.pack(pady=5)
        self.gift_lbl.bind("<Button-1>", lambda e: self.animate_open_gift())
        
        self.hint_lbl = tk.Label(
            center_frame,
            text="✨ Toca la caja de regalo para desatar el lazo y abrir la historia ✨",
            font=("Georgia", 11, "bold"),
            bg="#FFF2D6",
            fg=COLOR_ACCENT_RED,
            padx=16,
            pady=8,
            relief="flat"
        )
        self.hint_lbl.pack(pady=(12, 0))

    def animate_open_gift(self):
        self.gift_lbl.unbind("<Button-1>")
        self.play_sound_effect("ribbon.wav")
        self.hint_lbl.config(text="Desatando el lazo de terciopelo...")
        self.after(350, self._step_gift_opened)

    def _step_gift_opened(self):
        self.gift_lbl.config(image=self.img_gift_opened)
        self.play_sound_effect("chime.wav")
        self.hint_lbl.config(text="¡El libro de los Cien Acres se abre para ti! 📖✨")
        self.after(850, self.transition_to_storybook)

    def transition_to_storybook(self):
        self.current_state = "STORYBOOK"
        self.show_storybook_screen()

    # =========================================================================
    # PANTALLA 2: EL LIBRO DE CUENTOS ILUSTRADO
    # =========================================================================
    def show_storybook_screen(self):
        self.clear_frame()
        
        # 1. ENCABEZADO SUPERIOR CON BOTÓN DE MODO ESTUDIO Y MÚSICA
        header_frame = tk.Frame(self.root_frame, bg=COLOR_BANNER_BG, bd=1, relief="solid")
        header_frame.pack(fill="x", padx=15, pady=(6, 4))
        
        # Botón de carta secreta
        secret_btn = tk.Button(
            header_frame,
            image=self.img_honey_pot,
            compound="left",
            text=" Carta Secreta 🍯",
            font=FONT_BUTTON,
            bg="#FFECC0",
            fg=COLOR_TEXT_INK,
            activebackground="#FFDF9B",
            relief="flat",
            cursor="hand2",
            padx=8,
            pady=3,
            command=self.show_secret_letter_modal
        )
        secret_btn.pack(side="left", padx=(8, 4), pady=4)
        
        # BOTÓN ESPECIAL DE MODO ESTUDIO (DERECHO EN PERÚ)
        self.btn_study_mode = tk.Button(
            header_frame,
            text="⚖️ Modo Estudio (Derecho) 📖",
            font=("Segoe UI", 9, "bold"),
            bg="#FFF0B3" if not self.study_mode_active else "#E67E22",
            fg=COLOR_TEXT_INK if not self.study_mode_active else "#FFFFFF",
            activebackground="#FFD54F",
            relief="solid",
            bd=1,
            cursor="hand2",
            padx=10,
            pady=3,
            command=self.toggle_study_mode
        )
        self.btn_study_mode.pack(side="left", padx=4, pady=4)
        
        # Título de capítulo
        self.chap_title_lbl = tk.Label(
            header_frame,
            text="Capítulo Especial: De cómo los amigos del bosque vinieron a hablarte del amor y la vida",
            font=FONT_CHAPTER,
            bg=COLOR_BANNER_BG,
            fg=COLOR_TEXT_INK
        )
        self.chap_title_lbl.pack(side="left", expand=True, padx=4)
        
        # Selector de música (Pista 1 / 2 / 3)
        self.btn_cycle_track = tk.Button(
            header_frame,
            text=f"🎶 {TRACKS[self.current_track_idx][1]}",
            font=("Segoe UI", 8, "bold"),
            bg="#FFECC0",
            fg=COLOR_TEXT_INK,
            relief="flat",
            cursor="hand2",
            padx=8,
            pady=3,
            command=self.cycle_music_track
        )
        self.btn_cycle_track.pack(side="right", padx=(4, 8), pady=4)
        
        self.btn_music_toggle = tk.Button(
            header_frame,
            text="🔊 Sonando" if self.music_enabled else "🔇 Silencio",
            font=("Segoe UI", 8, "bold"),
            bg="#FFEFC8" if self.music_enabled else "#EAD8BA",
            fg=COLOR_TEXT_INK,
            relief="flat",
            cursor="hand2",
            padx=6,
            pady=3,
            command=self.toggle_music
        )
        self.btn_music_toggle.pack(side="right", pady=4)
        
        # 2. SELECTOR DE PERSONAJES (TABS)
        char_bar = tk.Frame(self.root_frame, bg=COLOR_PARCHMENT)
        char_bar.pack(fill="x", padx=15, pady=3)
        
        char_label = tk.Label(
            char_bar,
            text="Personaje:",
            font=("Georgia", 9, "bold"),
            bg=COLOR_PARCHMENT,
            fg="#7E6A58"
        )
        char_label.pack(side="left", padx=(5, 8))
        
        chars = [
            ("pooh", "🐻 Winnie the Pooh"),
            ("piglet", "🐷 Piglet"),
            ("eeyore", "🫏 Igor"),
            ("tigger", "🐯 Tigger"),
            ("christopher", "👦 Christopher"),
            ("rabbit", "🐰 Conejo"),
            ("owl", "🦉 Búho")
        ]
        
        self.char_buttons = {}
        for cid, label in chars:
            btn = tk.Button(
                char_bar,
                text=label,
                font=FONT_BUTTON,
                bg="#FFEFC8" if cid == self.current_char_id else "#F5EAD4",
                fg=COLOR_ACCENT_RED if cid == self.current_char_id else COLOR_TEXT_INK,
                relief="solid",
                bd=1,
                cursor="hand2",
                padx=7,
                pady=2,
                command=lambda c=cid: self.select_character(c)
            )
            btn.pack(side="left", padx=2)
            self.char_buttons[cid] = btn
            
        # 3. SELECTOR DE ESCENARIOS DE FONDO
        scenario_bar = tk.Frame(self.root_frame, bg=COLOR_PARCHMENT)
        scenario_bar.pack(fill="x", padx=15, pady=(1, 5))
        
        scen_label = tk.Label(
            scenario_bar,
            text="Fondo Escenario:",
            font=("Georgia", 9, "bold"),
            bg=COLOR_PARCHMENT,
            fg="#7E6A58"
        )
        scen_label.pack(side="left", padx=(5, 8))
        
        scenarios = [
            ("pooh_house", "🏡 Casa de Pooh"),
            ("bridge", "🌉 Puente de Piedra"),
            ("galleons_lap", "🌊 Tronco en Arroyo"),
            ("everest_forest", "🌳 Gran Bosque"),
            ("meadow_sun", "🌅 Prado del Sol"),
            ("honey_room", "🍯 Rincón de Miel")
        ]
        
        self.scen_buttons = {}
        for sid, label in scenarios:
            btn = tk.Button(
                scenario_bar,
                text=label,
                font=("Segoe UI", 8),
                bg="#FFF2D8" if sid == self.current_scenario_id else "#F8F1E4",
                fg=COLOR_TEXT_INK,
                relief="flat",
                cursor="hand2",
                padx=5,
                pady=2,
                command=lambda s=sid: self.select_scenario(s)
            )
            btn.pack(side="left", padx=2)
            self.scen_buttons[sid] = btn

        # 4. CUERPO PRINCIPAL DEL LIBRO
        book_frame = tk.Frame(self.root_frame, bg="#F5ECD8", bd=2, relief="solid")
        book_frame.pack(fill="both", expand=True, padx=15, pady=(0, 6))
        book_frame.columnconfigure(0, weight=4)
        book_frame.columnconfigure(1, weight=5)
        book_frame.rowconfigure(0, weight=1)
        
        # PÁGINA IZQUIERDA: ESCENARIO + POSES REACTIVAS
        left_page = tk.Frame(book_frame, bg=COLOR_PARCHMENT, padx=12, pady=8)
        left_page.grid(row=0, column=0, sticky="nsew", padx=(2, 1), pady=2)
        
        self.scenario_lbl = tk.Label(
            left_page,
            image=self.scenario_images[self.current_scenario_id],
            bg=COLOR_PARCHMENT,
            bd=1,
            relief="solid"
        )
        self.scenario_lbl.pack(fill="x", pady=(0, 4))
        
        self.scen_sub_lbl = tk.Label(
            left_page,
            text=wisdom_engine.SCENARIOS_DATA[self.current_scenario_id]["subtitle"],
            font=("Georgia", 9, "italic"),
            bg=COLOR_PARCHMENT,
            fg="#7E6C5C"
        )
        self.scen_sub_lbl.pack(pady=(0, 4))
        
        self.pose_caption_lbl = tk.Label(
            left_page,
            text="",
            font=("Georgia", 10, "italic"),
            bg="#FFF6E0",
            fg="#6B523F",
            wraplength=340,
            justify="center",
            padx=10,
            pady=4,
            relief="flat"
        )
        self.pose_caption_lbl.pack(fill="x", pady=(2, 4))
        
        self.char_img_lbl = tk.Label(
            left_page,
            bg=COLOR_PARCHMENT,
            cursor="hand2"
        )
        self.char_img_lbl.pack(pady=2)
        self.char_img_lbl.bind("<Button-1>", lambda e: self.cycle_character_pose())
        
        self.pose_counter_lbl = tk.Label(
            left_page,
            text="✨ Toca al personaje para cambiar su pose ✨",
            font=("Segoe UI", 9, "bold"),
            bg=COLOR_PARCHMENT,
            fg="#947D68"
        )
        self.pose_counter_lbl.pack(pady=(2, 4))
        
        self.btn_next_pose = tk.Button(
            left_page,
            text="Cambiar Pose 🐾",
            font=FONT_BUTTON,
            bg="#FFE8B5",
            fg=COLOR_TEXT_INK,
            activebackground="#FFDB94",
            relief="flat",
            cursor="hand2",
            padx=14,
            pady=5,
            command=self.cycle_character_pose
        )
        self.btn_next_pose.pack(pady=2)
        
        # PÁGINA DERECHA: CARTA / DIÁLOGO MANUSCRITO
        right_page = tk.Frame(book_frame, bg=COLOR_PARCHMENT, padx=16, pady=8)
        right_page.grid(row=0, column=1, sticky="nsew", padx=(1, 2), pady=2)
        
        card_box = tk.Frame(right_page, bg="#FFF9ED", bd=1, relief="solid", padx=16, pady=12)
        card_box.pack(fill="x", pady=(0, 6))
        
        self.badge_speaker = tk.Label(
            card_box,
            text="",
            font=("Georgia", 12, "bold"),
            bg="#FFE5B4",
            fg=COLOR_TEXT_INK,
            padx=10,
            pady=3
        )
        self.badge_speaker.pack(anchor="w", pady=(0, 6))
        
        self.lbl_quote = tk.Label(
            card_box,
            text="",
            font=("Georgia", 13, "italic"),
            bg="#FFF9ED",
            fg=COLOR_TEXT_INK,
            wraplength=430,
            justify="left",
            anchor="w"
        )
        self.lbl_quote.pack(fill="x", pady=6)
        
        sep = tk.Frame(card_box, bg=COLOR_BOOK_BORDER, height=1)
        sep.pack(fill="x", pady=5)
        
        self.lbl_lesson = tk.Label(
            card_box,
            text="",
            font=("Georgia", 10),
            bg="#FFF9ED",
            fg="#685545",
            wraplength=430,
            justify="left",
            anchor="w"
        )
        self.lbl_lesson.pack(fill="x", pady=(0, 3))
        
        self.lbl_context = tk.Label(
            card_box,
            text="",
            font=("Georgia", 9, "italic"),
            bg="#FFF9ED",
            fg="#948171",
            anchor="w"
        )
        self.lbl_context.pack(fill="x")
        
        # Botones de sentimientos rápidos / Modo Estudio
        self.quick_frame = tk.LabelFrame(
            right_page,
            text="  Preguntar sobre el corazón:  ",
            font=("Georgia", 9, "bold"),
            bg=COLOR_PARCHMENT,
            fg="#7E6C5C",
            padx=6,
            pady=4
        )
        self.quick_frame.pack(fill="x", pady=(0, 6))
        
        feelings = [
            ("❤️ Amor Verdadero", "amor"),
            ("🌧️ Día Gris", "triste"),
            ("🍃 Miedo & Valentía", "miedo"),
            ("⏳ Calma y Paciencia", "paciencia"),
            ("✨ Pequeños Detalles", "hoy")
        ]
        
        f_row = tk.Frame(self.quick_frame, bg=COLOR_PARCHMENT)
        f_row.pack(fill="x")
        for i, (label, tag) in enumerate(feelings):
            b = tk.Button(
                f_row,
                text=label,
                font=("Segoe UI", 8),
                bg="#FFF2D6",
                fg=COLOR_TEXT_INK,
                activebackground="#FFE4AC",
                relief="flat",
                cursor="hand2",
                padx=6,
                pady=3,
                command=lambda t=tag: self.ask_sentiment(t)
            )
            b.pack(side="left", padx=2, expand=True, fill="x")
            
        # Pregunta libre en la carta
        input_frame = tk.Frame(right_page, bg=COLOR_PARCHMENT)
        input_frame.pack(fill="x", pady=2)
        
        self.ask_lbl = tk.Label(
            input_frame,
            text="Escribe tus pensamientos o una pregunta sobre la vida:",
            font=("Georgia", 9, "bold"),
            bg=COLOR_PARCHMENT,
            fg="#7E6C5C"
        )
        self.ask_lbl.pack(anchor="w", pady=(0, 2))
        
        entry_row = tk.Frame(input_frame, bg=COLOR_PARCHMENT)
        entry_row.pack(fill="x")
        
        self.user_entry = tk.Entry(
            entry_row,
            font=("Segoe UI", 10),
            bg="#FFFFFF",
            fg=COLOR_TEXT_INK,
            relief="solid",
            bd=1
        )
        self.user_entry.pack(side="left", fill="x", expand=True, ipady=5, padx=(0, 6))
        self.user_entry.bind("<Return>", lambda e: self.on_ask_click())
        
        self.btn_ask = tk.Button(
            entry_row,
            text="Consultar 🍯",
            font=FONT_BUTTON,
            bg=COLOR_ACCENT_RED,
            fg="#FFFFFF",
            activebackground="#A82424",
            activeforeground="#FFFFFF",
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=5,
            command=self.on_ask_click
        )
        self.btn_ask.pack(side="right")
        
        self.select_character("pooh", play_sound=False)

    # =========================================================================
    # MODO ESTUDIO DE DERECHO (PERÚ)
    # =========================================================================
    def toggle_study_mode(self):
        self.study_mode_active = not self.study_mode_active
        self.play_sound_effect("chime.wav")
        
        if self.study_mode_active:
            # Poner música Lofi de Estudio (Pista 2)
            self.current_track_idx = 1
            if self.music_enabled:
                self.start_background_music()
            self.update_music_buttons()
            
            # Cambiar a Winnie the Pooh en pose pensando/estudio
            self.select_character("pooh", play_sound=False)
            self.char_pose_indices["pooh"] = 4 # Pose pensando
            self.update_character_pose_view()
            
            # Cambiar escenario a rincón cálido de lectura
            self.select_scenario("honey_room")
            
            # Actualizar botón y encabezado
            self.btn_study_mode.config(
                text="⚖️ MODO ESTUDIO: ACTIVO 📖",
                bg="#E67E22",
                fg="#FFFFFF"
            )
            self.chap_title_lbl.config(
                text="⚖️ Modo Estudio: Winnie the Pooh te acompaña en tus lecturas de Derecho 🇵🇪"
            )
            self.btn_next_pose.config(text="☕ Otro Consejo para Estudiar 🍯")
            
            # Mostrar primer consejo filosófico de estudio
            law_quote = wisdom_engine.get_random_law_study_quote()
            self.display_quote_animated(law_quote)
        else:
            self.btn_study_mode.config(
                text="⚖️ Modo Estudio (Derecho) 📖",
                bg="#FFF0B3",
                fg=COLOR_TEXT_INK
            )
            self.chap_title_lbl.config(
                text="Capítulo Especial: De cómo los amigos del bosque vinieron a hablarte del amor y la vida"
            )
            char_info = wisdom_engine.get_character_info(self.current_char_id)
            self.btn_next_pose.config(text=f"Cambiar Pose de {char_info['name'].split()[0]} 🐾")
            
            # Restaurar cita normal
            quote_data = wisdom_engine.get_random_quote_for_character(self.current_char_id)
            self.display_quote_animated(quote_data)

    # =========================================================================
    # ACCIONES: CAMBIO DE POSES REACTIVO Y CAMBIO DE PERSONAJE
    # =========================================================================
    def select_character(self, char_id, play_sound=True):
        self.current_char_id = char_id
        if play_sound:
            self.play_sound_effect("pop.wav")
            
        for cid, btn in self.char_buttons.items():
            if cid == char_id:
                btn.config(bg="#FFEFC8", fg=COLOR_ACCENT_RED)
            else:
                btn.config(bg="#F5EAD4", fg=COLOR_TEXT_INK)
                
        char_info = wisdom_engine.get_character_info(char_id)
        if not self.study_mode_active:
            self.btn_next_pose.config(text=f"Cambiar Pose de {char_info['name'].split()[0]} 🐾")
        else:
            self.btn_next_pose.config(text="☕ Otro Consejo para Estudiar 🍯")
            
        self.update_character_pose_view()
        
        if self.study_mode_active and char_id == "pooh":
            quote_data = wisdom_engine.get_random_law_study_quote()
        else:
            quote_data = wisdom_engine.get_random_quote_for_character(char_id)
        self.display_quote_animated(quote_data)

    def cycle_character_pose(self):
        poses = self.character_poses.get(self.current_char_id, [])
        if not poses:
            return
            
        self.char_pose_indices[self.current_char_id] = (self.char_pose_indices[self.current_char_id] + 1) % len(poses)
        self.play_sound_effect("pop.wav")
        
        self.update_character_pose_view()
        
        self.char_img_lbl.pack_configure(pady=(0, 4))
        self.after(90, lambda: self.char_img_lbl.pack_configure(pady=2))
        
        if self.study_mode_active and self.current_char_id == "pooh":
            quote_data = wisdom_engine.get_random_law_study_quote()
        else:
            quote_data = wisdom_engine.get_random_quote_for_character(self.current_char_id)
        self.display_quote_animated(quote_data)

    def update_character_pose_view(self):
        poses = self.character_poses.get(self.current_char_id, [])
        if not poses:
            return
            
        idx = self.char_pose_indices[self.current_char_id] % len(poses)
        img_tk, caption = poses[idx]
        
        self.char_img_lbl.config(image=img_tk)
        self.pose_caption_lbl.config(text=caption)
        self.pose_counter_lbl.config(text=f"✨ Pose {idx + 1} de {len(poses)} — Toca el dibujo para cambiar ✨")

    def select_scenario(self, scen_id):
        self.current_scenario_id = scen_id
        self.play_sound_effect("pop.wav")
        
        for sid, btn in self.scen_buttons.items():
            if sid == scen_id:
                btn.config(bg="#FFF2D8", relief="solid", bd=1)
            else:
                btn.config(bg="#F8F1E4", relief="flat", bd=0)
                
        if scen_id in self.scenario_images:
            self.scenario_lbl.config(image=self.scenario_images[scen_id])
            self.scen_sub_lbl.config(text=wisdom_engine.SCENARIOS_DATA[scen_id]["subtitle"])

    def ask_sentiment(self, tag):
        self.play_sound_effect("pop.wav")
        wisdom = wisdom_engine.analyze_and_get_wisdom(tag, self.current_char_id)
        target_char = wisdom.get("char_id", self.current_char_id)
        if target_char != self.current_char_id:
            self.select_character(target_char, play_sound=False)
        else:
            self.cycle_character_pose()
        self.display_quote_animated(wisdom)

    def on_ask_click(self):
        query = self.user_entry.get().strip()
        self.user_entry.delete(0, tk.END)
        self.ask_sentiment(query)

    def display_quote_animated(self, data):
        if self.typewriter_job:
            self.after_cancel(self.typewriter_job)
            self.typewriter_job = None
            
        speaker = data.get("speaker", "Winnie the Pooh")
        title = data.get("title", "")
        quote = data.get("quote", "")
        lesson = data.get("lesson", "")
        context = data.get("context", "")
        
        self.badge_speaker.config(text=f"{speaker} — {title}")
        self.lbl_quote.config(text="")
        self.lbl_lesson.config(text="")
        self.lbl_context.config(text="")
        
        self._typewriter_step(quote, lesson, context, 0)

    def _typewriter_step(self, quote, lesson, context, idx):
        if idx <= len(quote):
            self.lbl_quote.config(text=quote[:idx])
            self.typewriter_job = self.after(16, lambda: self._typewriter_step(quote, lesson, context, idx + 1))
        else:
            self.lbl_lesson.config(text=f"💡 Enseñanza de Vida: {lesson}")
            if context:
                self.lbl_context.config(text=f"📜 {context}")
            self.typewriter_job = None

    # =========================================================================
    # MODAL: CARTA SECRETA DEDICADA
    # =========================================================================
    def show_secret_letter_modal(self):
        letter_data = wisdom_engine.get_secret_letter()
        self.play_sound_effect("chime.wav")
        
        modal = tk.Toplevel(self)
        modal.title("Una Carta Especial para Ti 🍯")
        modal.geometry("560x500")
        modal.configure(bg="#FFFDF6")
        modal.transient(self)
        modal.grab_set()
        
        mx = self.winfo_x() + (self.winfo_width() - 560) // 2
        my = self.winfo_y() + (self.winfo_height() - 500) // 2
        modal.geometry(f"+{mx}+{my}")
        
        border_frame = tk.Frame(modal, bg=COLOR_ACCENT_GOLD, bd=2, relief="groove")
        border_frame.pack(fill="both", expand=True, padx=16, pady=16)
        
        inner_frame = tk.Frame(border_frame, bg="#FFF9EB", padx=22, pady=18)
        inner_frame.pack(fill="both", expand=True)
        
        lbl_title = tk.Label(
            inner_frame,
            text=letter_data["title"],
            font=("Georgia", 15, "bold"),
            bg="#FFF9EB",
            fg=COLOR_TEXT_INK
        )
        lbl_title.pack(pady=(0, 12))
        
        lbl_body = tk.Label(
            inner_frame,
            text=letter_data["content"],
            font=("Georgia", 11, "italic"),
            bg="#FFF9EB",
            fg=COLOR_TEXT_INK,
            wraplength=460,
            justify="left",
            anchor="w"
        )
        lbl_body.pack(fill="both", expand=True, pady=5)
        
        btn_close = tk.Button(
            inner_frame,
            text="Guardar en el Corazón ❤️",
            font=FONT_BUTTON,
            bg=COLOR_ACCENT_RED,
            fg="#FFFFFF",
            activebackground="#A82424",
            relief="flat",
            cursor="hand2",
            padx=16,
            pady=8,
            command=modal.destroy
        )
        btn_close.pack(pady=(12, 0))

    def clear_frame(self):
        if self.typewriter_job:
            self.after_cancel(self.typewriter_job)
            self.typewriter_job = None
        for w in self.root_frame.winfo_children():
            w.destroy()

if __name__ == "__main__":
    app = WinniePoohStorybookApp()
    app.mainloop()
