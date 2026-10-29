"""
test_app_v2.py - Verificación de todas las nuevas funcionalidades
1. Comprueba los 7 personajes 2D y los 6 fondos de escenarios.
2. Comprueba los 4 archivos de audio de alto volumen.
3. Comprueba las citas de todos los personajes y el motor de búsqueda temática.
"""

import os
import sys

sys.path.append(r"C:\Users\LENOVO\.gemini\antigravity\scratch\winnie_pooh_gift")
import wisdom_engine

def test_all_assets():
    assets_dir = r"C:\Users\LENOVO\.gemini\antigravity\scratch\winnie_pooh_gift\assets"
    
    # 7 Personajes
    chars = ["char_pooh.png", "char_piglet.png", "char_eeyore.png", "char_tigger.png",
             "char_christopher.png", "char_rabbit.png", "char_owl.png"]
    for c in chars:
        p = os.path.join(assets_dir, c)
        assert os.path.exists(p), f"Falta personaje: {c}"
        assert os.path.getsize(p) > 2000
        
    # 6 Escenarios
    scenarios = ["bg_pooh_house.png", "bg_bridge.png", "bg_gloomy_place.png",
                 "bg_bee_tree.png", "bg_rabbit_garden.png", "bg_galleons_lap.png"]
    for s in scenarios:
        p = os.path.join(assets_dir, s)
        assert os.path.exists(p), f"Falta escenario: {s}"
        assert os.path.getsize(p) > 2000
        
    # 4 Archivos de audio
    audios = ["music_theme.wav", "chime.wav", "pop.wav", "ribbon.wav"]
    for a in audios:
        p = os.path.join(assets_dir, a)
        assert os.path.exists(p), f"Falta audio: {a}"
        assert os.path.getsize(p) > 5000
        
    print("[PASS] Todos los 17 assets (personajes, fondos y audio) verificados.")

def test_characters_wisdom():
    all_chars = ["pooh", "piglet", "eeyore", "tigger", "christopher", "rabbit", "owl"]
    total_quotes = 0
    for cid in all_chars:
        info = wisdom_engine.get_character_info(cid)
        quotes = wisdom_engine.get_character_quotes(cid)
        assert len(quotes) >= 2, f"Pocas citas para {cid}"
        total_quotes += len(quotes)
        # Probar selección aleatoria
        q = wisdom_engine.get_random_quote_for_character(cid)
        assert "quote" in q and "lesson" in q and "speaker" in q
    print(f"[PASS] {total_quotes} citas icónicas verificadas a lo largo de los 7 personajes.")

def test_theme_search():
    queries = ["amor verdadero", "lluvia y tristeza", "miedo al futuro", "paciencia", "pequeños momentos"]
    for q in queries:
        res = wisdom_engine.analyze_and_get_wisdom(q)
        assert "quote" in res and "speaker" in res
    print("[PASS] Búsqueda temática del libro probada con éxito.")

if __name__ == "__main__":
    test_all_assets()
    test_characters_wisdom()
    test_theme_search()
    print(">>> TODOS LOS TESTS DE LA V2 PASARON CON ÉXITO <<<")
