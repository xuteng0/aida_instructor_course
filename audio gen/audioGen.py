import numpy as np
import wave
import os

# Global variables
waveform_type = 'sine'  # Choose between 'sine', 'square', 'triangle', or 'white_noise'
frequency = 5000  # Frequency for the tone (Hz)
duration = 15  # Total duration of the audio (seconds)
channels = 'left'  # Choose between 'left', 'right', or 'stereo'

# Parameters
sample_rate = 44100  # Samples per second

# Function to generate audio signal
def generate_signal():
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(time)

    # Generate waveform based on the type
    if waveform_type == 'sine':
        signal = np.sin(2 * np.pi * frequency * time)
    elif waveform_type == 'square':
        signal = np.sign(np.sin(2 * np.pi * frequency * time))
    elif waveform_type == 'triangle':
        signal = 2 * np.abs(np.mod(time * frequency, 1) - 0.5) - 1
    elif waveform_type == 'white_noise':
        signal = np.random.normal(0, 1, len(time))
    else:
        raise ValueError("Invalid waveform type. Choose from 'sine', 'square', 'triangle', or 'white_noise'.")

    # Normalize the signal to 16-bit PCM range
    signal = np.int16(signal / np.max(np.abs(signal)) * 32767)

    return signal

# Function to create stereo signal
def create_stereo_signal(signal):
    stereo_signal = np.zeros((len(signal), 2), dtype=np.int16)
    if channels == 'left':
        stereo_signal[:, 0] = signal  # Left channel
        stereo_signal[:, 1] = 0  # Right channel silent
    elif channels == 'right':
        stereo_signal[:, 0] = 0  # Left channel silent
        stereo_signal[:, 1] = signal  # Right channel
    elif channels == 'stereo':
        stereo_signal[:, 0] = signal  # Left channel
        stereo_signal[:, 1] = signal  # Right channel
    else:
        raise ValueError("Invalid channel configuration. Choose from 'left', 'right', or 'stereo'.")
    return stereo_signal

# Function to save the audio file
def save_audio():
    signal = generate_signal()
    stereo_signal = create_stereo_signal(signal)
    # Generate the file name based on the global variables
    file_name = f"audio_{waveform_type}_{frequency}Hz_{channels}_{duration}s.wav"
    # Get the folder of the script to save the file
    script_folder = os.path.dirname(os.path.realpath(__file__))
    output_file = os.path.join(script_folder, file_name)
    # Save the audio file
    with wave.open(output_file, 'w') as wav_file:
        wav_file.setnchannels(2)  # Stereo
        wav_file.setsampwidth(2)  # 2 bytes (16-bit)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(stereo_signal.tobytes())
    print(f"Audio file saved as {output_file}")

if __name__ == '__main__':
    save_audio()
