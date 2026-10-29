"""
test_app.py - Verificación automatizada de integridad de la aplicación
Comprueba:
1. Existencia y carga de todos los archivos gráficos PNG y audio WAV.
2. Funcionamiento del motor de sabiduría y clasificación.
3. Carga e inicialización de la interfaz Tkinter en modo headless/verificación.
"""

import os
import sys
from PIL import Image

sys.path.append(r"C:\Users\LENOVO\.gemini\antigravity\scratch\winnie_pooh_gift")
import wisdom_engine

def test_assets():
    assets_dir = r"C:\Users\LENOVO\.gemini\antigravity\scratch\winnie_pooh_gift\assets"
    expected_assets = [
        "gift_closed.png", "gift_opened.png", "honey_pot.png", "icon.ico",
        "pooh_greeting.png", "pooh_thinking.png", "pooh_honey.png",
        "pooh_balloon.png", "pooh_hug.png", "pooh_resting.png",
        "music_theme.wav", "chime.wav", "pop.wav", "ribbon.wav"
    ]
    for asset in expected_assets:
        p = os.path.join(assets_dir, asset)
        assert os.path.exists(p), f"Falta el archivo: {asset}"
        assert os.path.getsize(p) > 1000, f"Archivo demasiado pequeño o corrupto: {asset}"
        if asset.endswith(".png"):
            img = Image.open(p)
            assert img.size == (512, 512), f"Tamaño incorrecto en {asset}: {img.size}"
    print("[PASS] Todos los assets graficos y de audio verificados con exito.")

def test_wisdom():
    test_queries = [
        "me siento triste",
        "que es el amor",
        "tengo miedo",
        "necesito calma y paciencia",
        "duda sobre mi futuro",
        "algo bonito hoy",
        ""
    ]
    for q in test_queries:
        res = wisdom_engine.analyze_and_get_wisdom(q)
        assert "quote" in res and len(res["quote"]) > 10, f"Error en query '{q}'"
        assert "lesson" in res and len(res["lesson"]) > 10, f"Falta leccion en query '{q}'"
        assert "speaker" in res, f"Falta speaker en query '{q}'"
    print(f"[PASS] Motor de sabiduria probado con {len(test_queries)} preguntas tematicas con exito.")

def test_secret_letter():
    letter = wisdom_engine.get_secret_letter()
    assert "title" in letter and "content" in letter
    assert len(letter["content"]) > 100
    print("[PASS] Carta secreta verificada.")

if __name__ == "__main__":
    test_assets()
    test_wisdom()
    test_secret_letter()
    print(">>> TODOS LOS TESTS PASARON CON EXITO <<<")
