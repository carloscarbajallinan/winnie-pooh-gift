"""
generate_audio.py - Generador determinista de efectos y música de caja de música
Produce archivos WAV de alta calidad (16-bit 44.1kHz estéreo) sin dependencias externas:
1. music_theme.wav: Melodía nostálgica y dulce en caja de música / piano de cuna.
2. chime.wav: Carillón mágico al abrir el regalo.
3. pop.wav: Sonido suave de 'plop' al cambiar de pose.
4. ribbon.wav: Sonido suave de desatar la cinta.
"""

import math
import struct
import wave
import os

SAMPLE_RATE = 44100

def create_music_box_note(freq, duration, volume=0.45):
    """Genera una nota de caja de música con armónicos metálicos y decaimiento exponencial"""
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    decay = 4.5  # Tasa de decaimiento natural de lámina metálica
    
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        # Envolvente de ataque instantáneo y caída exponencial
        envelope = math.exp(-decay * t)
        
        # Fundamental + armónicos de celesta / chime
        val = (
            math.sin(2 * math.pi * freq * t) * 0.70 +
            math.sin(2 * math.pi * freq * 2.0 * t) * 0.20 +
            math.sin(2 * math.pi * freq * 3.01 * t) * 0.07 +
            math.sin(2 * math.pi * freq * 4.2 * t) * 0.03
        )
        sample = val * envelope * volume
        # Clamp
        sample = max(-0.99, min(0.99, sample))
        int_sample = int(sample * 32767)
        samples.append(int_sample)
    return samples

def write_wav(filename, samples, channels=1):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        data = bytearray()
        for s in samples:
            data.extend(struct.pack('<h', s))
        wf.writeframes(data)

def generate_lullaby_theme(filepath):
    """
    Genera una melodía dulce, tierna y nostálgica inspirada en el tema del bosque de los Cien Acres.
    Escala Pentatónica Mayor cálida (Do Mayor / Fa Mayor).
    """
    # Notas (Frecuencias en Hz)
    C4 = 261.63; D4 = 293.66; E4 = 329.63; F4 = 349.23; G4 = 392.00; A4 = 440.00; B4 = 493.88
    C5 = 523.25; D5 = 587.33; E5 = 659.25; F5 = 698.46; G5 = 783.99; A5 = 880.00
    
    # Secuencia de melodía dulce de caja de música (nota, duracion_seg)
    melody = [
        # Frase 1: Dulce despertar
        (C5, 0.45), (E5, 0.45), (G5, 0.8), (E5, 0.45), (C5, 0.45),
        (A4, 0.45), (C5, 0.45), (G4, 1.1),
        # Frase 2: Pequeña reflexión de Pooh
        (E4, 0.45), (G4, 0.45), (C5, 0.8), (D5, 0.45), (C5, 0.45),
        (B4, 0.45), (A4, 0.45), (G4, 1.2),
        # Frase 3: Vals del Bosque
        (C5, 0.45), (D5, 0.45), (E5, 0.8), (G5, 0.8),
        (F5, 0.45), (E5, 0.45), (D5, 0.8), (C5, 1.0),
        # Frase 4: El tarrito de miel
        (A4, 0.45), (C5, 0.45), (E5, 0.8), (D5, 0.6),
        (C5, 0.45), (B4, 0.45), (C5, 1.5),
        # Pausa tierna
        (0, 0.6)
    ]
    
    total_samples = []
    for note, dur in melody:
        if note == 0:
            total_samples.extend([0] * int(SAMPLE_RATE * dur))
        else:
            total_samples.extend(create_music_box_note(note, dur, volume=0.4))
            
    write_wav(filepath, total_samples)

def generate_magic_chime(filepath):
    """Sonido mágico de apertura con campanillas ascendentes y reverberación"""
    notes = [523.25, 659.25, 783.99, 1046.50, 1318.51, 1567.98]
    total_samples = [0] * int(SAMPLE_RATE * 2.2)
    
    for i, freq in enumerate(notes):
        offset = int(SAMPLE_RATE * (i * 0.09))
        note_samples = create_music_box_note(freq, 1.4, volume=0.35)
        for j, s in enumerate(note_samples):
            if offset + j < len(total_samples):
                total_samples[offset + j] += s
                
    # Normalizar para evitar clipping
    max_val = max(abs(s) for s in total_samples) or 1
    total_samples = [int((s / max_val) * 28000) for s in total_samples]
    write_wav(filepath, total_samples)

def generate_pop(filepath):
    """Sonido tierno y sutil de 'plop' con pitch bend rápido hacia abajo"""
    n_samples = int(SAMPLE_RATE * 0.15)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        freq = 600 - 350 * (t / 0.15) # De 600Hz a 250Hz rápido
        envelope = math.exp(-22 * t)
        sample = math.sin(2 * math.pi * freq * t) * envelope * 0.5
        samples.append(int(sample * 32767))
    write_wav(filepath, samples)

def generate_ribbon(filepath):
    """Sonido de deslizar cinta / lazo suave"""
    n_samples = int(SAMPLE_RATE * 0.35)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        # Ruido suave filtrado con tono sutil
        envelope = math.sin(math.pi * (t / 0.35))
        freq = 800 + 400 * math.sin(15 * t)
        sample = (math.sin(2 * math.pi * freq * t) * 0.3 + (math.sin(12345 * t) % 0.2)) * envelope * 0.35
        samples.append(int(sample * 32767))
    write_wav(filepath, samples)

if __name__ == "__main__":
    assets_dir = r"C:\Users\LENOVO\.gemini\antigravity\scratch\winnie_pooh_gift\assets"
    os.makedirs(assets_dir, exist_ok=True)
    generate_lullaby_theme(os.path.join(assets_dir, "music_theme.wav"))
    generate_magic_chime(os.path.join(assets_dir, "chime.wav"))
    generate_pop(os.path.join(assets_dir, "pop.wav"))
    generate_ribbon(os.path.join(assets_dir, "ribbon.wav"))
    print("All audio assets generated successfully in", assets_dir)
