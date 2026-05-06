"""Procedural audio generation for calming sounds and binaural beats."""
import numpy as np
from scipy.io import wavfile
import io
import base64
import streamlit as st

SAMPLE_RATE = 44100

def generate_tone(freq, duration, volume=0.3, fade_in=0.5, fade_out=0.5):
    """Generate a sine wave tone with fade in/out."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = np.sin(2 * np.pi * freq * t) * volume

    # Apply fade in/out
    fade_in_samples = int(SAMPLE_RATE * fade_in)
    fade_out_samples = int(SAMPLE_RATE * fade_out)

    if fade_in_samples > 0:
        wave[:fade_in_samples] *= np.linspace(0, 1, fade_in_samples)
    if fade_out_samples > 0:
        wave[-fade_out_samples:] *= np.linspace(1, 0, fade_out_samples)

    return wave.astype(np.float32)

def generate_binaural_beat(base_freq, beat_freq, duration, volume=0.2):
    """Generate binaural beats for brainwave entrainment."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    left = np.sin(2 * np.pi * base_freq * t) * volume
    right = np.sin(2 * np.pi * (base_freq + beat_freq) * t) * volume

    stereo = np.vstack((left, right)).T
    return stereo.astype(np.float32)

def generate_white_noise(duration, volume=0.1):
    """Generate white noise."""
    samples = int(SAMPLE_RATE * duration)
    noise = np.random.normal(0, 1, samples) * volume
    return noise.astype(np.float32)

def generate_brown_noise(duration, volume=0.15):
    """Generate brown noise (deeper, warmer than white noise)."""
    samples = int(SAMPLE_RATE * duration)
    white = np.random.normal(0, 1, samples)
    brown = np.cumsum(white)
    brown = brown / np.max(np.abs(brown)) * volume
    return brown.astype(np.float32)

def generate_pink_noise(duration, volume=0.12):
    """Generate pink noise (balanced, natural sounding)."""
    samples = int(SAMPLE_RATE * duration)
    white = np.random.normal(0, 1, samples)
    # Simple pink noise approximation using cumulative sum with decay
    pink = np.cumsum(white)
    pink = pink / np.max(np.abs(pink)) * volume
    # Additional filtering for pink characteristics
    pink = np.convolve(pink, np.ones(10)/10, mode='same')
    return pink.astype(np.float32)

def generate_rain_sound(duration, volume=0.2):
    """Generate rain-like sound using filtered noise."""
    samples = int(SAMPLE_RATE * duration)
    noise = np.random.normal(0, 1, samples)
    # Low-pass filter effect using moving average
    window = 50
    rain = np.convolve(noise, np.ones(window)/window, mode='same')
    rain = rain / np.max(np.abs(rain)) * volume
    return rain.astype(np.float32)

def generate_ocean_waves(duration, volume=0.2):
    """Generate ocean wave sound using amplitude modulation."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    # Slow amplitude modulation (0.1 Hz = 10 second waves)
    carrier = np.random.normal(0, 1, len(t))
    modulator = (np.sin(2 * np.pi * 0.1 * t) + 1) / 2
    ocean = carrier * modulator * volume
    # Smooth with moving average
    ocean = np.convolve(ocean, np.ones(100)/100, mode='same')
    ocean = ocean / np.max(np.abs(ocean)) * volume
    return ocean.astype(np.float32)

def generate_isochronic_tone(base_freq, pulse_freq, duration, volume=0.25):
    """Generate isochronic tones (stronger than binaural, no headphones needed)."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    tone = np.sin(2 * np.pi * base_freq * t)
    pulse = (np.sin(2 * np.pi * pulse_freq * t) > 0).astype(float)
    isochronic = tone * pulse * volume
    return isochronic.astype(np.float32)

def generate_sleep_story_bg(duration, volume=0.08):
    """Generate very soft ambient background for sleep stories."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    # Very slow moving pads
    pad1 = np.sin(2 * np.pi * 110 * t) * np.sin(2 * np.pi * 0.05 * t) * volume * 0.5
    pad2 = np.sin(2 * np.pi * 164 * t) * np.sin(2 * np.pi * 0.03 * t + 1) * volume * 0.5
    pad3 = np.sin(2 * np.pi * 196 * t) * np.sin(2 * np.pi * 0.07 * t + 2) * volume * 0.3
    bg = (pad1 + pad2 + pad3) / 3
    return bg.astype(np.float32)

def audio_to_bytes(audio_data, sample_rate=SAMPLE_RATE):
    """Convert numpy array to WAV bytes for Streamlit audio player."""
    # Ensure audio is in correct range
    if audio_data.dtype != np.int16:
        audio_data = np.clip(audio_data, -1, 1)
        audio_data = (audio_data * 32767).astype(np.int16)

    buffer = io.BytesIO()
    wavfile.write(buffer, sample_rate, audio_data)
    buffer.seek(0)
    return buffer.read()

def get_audio_player(audio_data, sample_rate=SAMPLE_RATE):
    """Get Streamlit audio player component."""
    audio_bytes = audio_to_bytes(audio_data, sample_rate)
    return audio_bytes

# Predefined sound presets
SOUND_PRESETS = {
    "White Noise": lambda d: generate_white_noise(d),
    "Brown Noise": lambda d: generate_brown_noise(d),
    "Pink Noise": lambda d: generate_pink_noise(d),
    "Rain": lambda d: generate_rain_sound(d),
    "Ocean Waves": lambda d: generate_ocean_waves(d),
    "Deep Sleep (Delta)": lambda d: generate_binaural_beat(100, 2.5, d),
    "Meditation (Theta)": lambda d: generate_binaural_beat(200, 6, d),
    "Focus (Alpha)": lambda d: generate_binaural_beat(250, 10, d),
    "Calm (Alpha-Theta)": lambda d: generate_binaural_beat(180, 7, d),
    "Sleep Story Ambient": lambda d: generate_sleep_story_bg(d),
}

BREATHING_GUIDES = {
    "4-7-8 Relaxation": {"inhale": 4, "hold": 7, "exhale": 8, "cycles": 4},
    "Box Breathing (4-4-4-4)": {"inhale": 4, "hold": 4, "exhale": 4, "hold2": 4, "cycles": 5},
    "Coherent Breathing (5-5)": {"inhale": 5, "hold": 0, "exhale": 5, "cycles": 6},
    "Physiological Sigh": {"inhale": 2, "inhale2": 1.5, "exhale": 5, "cycles": 3},
    "Energizing (4-2-4)": {"inhale": 4, "hold": 2, "exhale": 4, "cycles": 5},
}
