"""
generate_audio_v2.py - Generador de audio de ALTO VOLUMEN y máxima claridad
Crea archivos WAV 16-bit 44.1kHz normalizados a 95% de amplitud máxima:
1. music_theme.wav: Melodía de caja de música/celesta con armónicos ricos y alto volumen.
2. chime.wav: Campanas mágicas cristalinas y sonoras.
3. pop.wav: Sonido suave de cambio de página / pose.
4. ribbon.wav: Sonido de desatar la cinta.
"""

import math
import struct
import wave
import os

SAMPLE_RATE = 44100
ASSETS_DIR = r"C:\Users\LENOVO\.gemini\antigravity\scratch\winnie_pooh_gift\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def write_wav_normalized(filename, raw_samples, max_amp=31000):
    """Escribe samples normalizados a 95% de la escala de 16-bit (máximo volumen sin distorsión)"""
    if not raw_samples:
        return
    peak = max(abs(s) for s in raw_samples)
    if peak == 0:
        peak = 1.0
    scale = max_amp / peak
    
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono para máxima compatibilidad con todos los drivers
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        data = bytearray()
        for s in raw_samples:
            scaled = int(s * scale)
            scaled = max(-32767, min(32767, scaled))
            data.extend(struct.pack('<h', scaled))
        wf.writeframes(data)

def music_box_note(freq, duration, decay=3.2):
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        env = math.exp(-decay * t)
        # Campana metálica de caja de música tradicional con armónicos
        v = (
            math.sin(2 * math.pi * freq * t) * 0.70 +
            math.sin(2 * math.pi * freq * 2.0 * t) * 0.22 +
            math.sin(2 * math.pi * freq * 3.0 * t) * 0.10 +
            math.sin(2 * math.pi * freq * 4.16 * t) * 0.05
        )
        samples.append(v * env)
    return samples

def generate_loud_theme():
    # Notas (Frecuencias en Hz)
    C4 = 261.63; D4 = 293.66; E4 = 329.63; F4 = 349.23; G4 = 392.00; A4 = 440.00; B4 = 493.88
    C5 = 523.25; D5 = 587.33; E5 = 659.25; F5 = 698.46; G5 = 783.99; A5 = 880.00
    
    # Melodía de caja de música cálida y dulce de Winnie the Pooh
    melody = [
        # Frase 1: El despertar en el Bosque
        (C5, 0.45), (E5, 0.45), (G5, 0.8), (E5, 0.45), (C5, 0.45),
        (A4, 0.45), (C5, 0.45), (G4, 1.0),
        # Acompañamiento bajo tierno
        (E4, 0.45), (G4, 0.45), (C5, 0.8), (D5, 0.45), (C5, 0.45),
        (B4, 0.45), (A4, 0.45), (G4, 1.1),
        # Frase 2: Un tarrito de miel
        (C5, 0.45), (D5, 0.45), (E5, 0.7), (G5, 0.8),
        (F5, 0.45), (E5, 0.45), (D5, 0.7), (C5, 0.9),
        # Frase 3: La despedida dulce
        (A4, 0.45), (C5, 0.45), (E5, 0.7), (D5, 0.6),
        (C5, 0.45), (B4, 0.45), (C5, 1.4),
        (0, 0.5)
    ]
    
    samples = []
    for freq, dur in melody:
        if freq == 0:
            samples.extend([0.0] * int(SAMPLE_RATE * dur))
        else:
            samples.extend(music_box_note(freq, dur))
            
    filepath = os.path.join(ASSETS_DIR, "music_theme.wav")
    write_wav_normalized(filepath, samples)
    print("music_theme.wav (ALTO VOLUMEN) generado OK")

def generate_loud_chime():
    notes = [523.25, 659.25, 783.99, 1046.50, 1318.51, 1567.98]
    total_len = int(SAMPLE_RATE * 2.0)
    samples = [0.0] * total_len
    for i, freq in enumerate(notes):
        offset = int(SAMPLE_RATE * (i * 0.08))
        note_s = music_box_note(freq, 1.4, decay=2.5)
        for j, s in enumerate(note_s):
            if offset + j < total_len:
                samples[offset + j] += s
    write_wav_normalized(os.path.join(ASSETS_DIR, "chime.wav"), samples)
    print("chime.wav (ALTO VOLUMEN) generado OK")

def generate_loud_pop():
    n_samples = int(SAMPLE_RATE * 0.16)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        freq = 650 - 380 * (t / 0.16)
        env = math.exp(-18 * t)
        samples.append(math.sin(2 * math.pi * freq * t) * env)
    write_wav_normalized(os.path.join(ASSETS_DIR, "pop.wav"), samples)
    print("pop.wav (ALTO VOLUMEN) generado OK")

def generate_loud_ribbon():
    n_samples = int(SAMPLE_RATE * 0.35)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        env = math.sin(math.pi * (t / 0.35))
        freq = 900 + 350 * math.sin(18 * t)
        val = math.sin(2 * math.pi * freq * t) * env
        samples.append(val)
    write_wav_normalized(os.path.join(ASSETS_DIR, "ribbon.wav"), samples)
    print("ribbon.wav (ALTO VOLUMEN) generado OK")

if __name__ == "__main__":
    generate_loud_theme()
    generate_loud_chime()
    generate_loud_pop()
    generate_loud_ribbon()
