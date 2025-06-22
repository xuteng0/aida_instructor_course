import numpy as np
import wave
import os

# Global variables
waveform_type = 'sine'  # Choose between 'sine', 'square', 'triangle', or 'white_noise'
frequency = 100  # Frequency for periodic waves (Hz)
duration_on = 0.02  # Duration of the waveform "on" (seconds)
duration_off = 0.02  # Duration of the waveform "off" (seconds)
fade_duration = 0.01  # Duration of fade-out (seconds)
duration = 15  # Total duration of the audio (seconds)
channels = 'stereo'  # Choose between 'left', 'right', or 'stereo'

# Parameters
sample_rate = 44100  # Samples per second

# Function to generate audio signal with fade-out effect
def generate_signal():
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(time)

    # Generate waveform based on the type
    for i in range(0, len(time), int(sample_rate * (duration_on + duration_off))):
        # Signal generation for the "on" period
        start = i
        end = i + int(sample_rate * duration_on)
        
        if waveform_type == 'sine':
            signal[start:end] = np.sin(2 * np.pi * frequency * time[start:end])
        elif waveform_type == 'square':
            signal[start:end] = np.sign(np.sin(2 * np.pi * frequency * time[start:end]))
        elif waveform_type == 'triangle':
            signal[start:end] = 2 * np.abs(np.mod(time[start:end] * frequency, 1) - 0.5) - 1
        elif waveform_type == 'white_noise':
            signal[start:end] = np.random.normal(0, 1, int(sample_rate * duration_on))
        else:
            raise ValueError("Invalid waveform type. Choose from 'sine', 'square', 'triangle', or 'white_noise'.")

        # Apply fade-out to the last part of the "on" segment
        fade_samples = int(sample_rate * fade_duration)
        fade_start = end - fade_samples
        fade = np.linspace(1, 0, fade_samples)
        signal[fade_start:end] *= fade

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
    file_name = f"audio_{waveform_type}_{frequency}Hz_{channels}_{duration_on}s_on_{duration_off}s_off_{fade_duration}s_fade_{duration}s.wav"
    
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
