import numpy as np
from scipy.signal import butter, filtfilt
import soundfile as sf

def apply_audio_filter(input_signal, key, cutoff_frequency=1000, sampling_rate=44100):
    """
    Apply a high-pass or low-pass filter to an input audio signal.

    Parameters:
    - input_signal (numpy array): The input audio signal.
    - key (str): The key variable to select the filter ('highpass' or 'lowpass').
    - cutoff_frequency (float): The cutoff frequency for the filter in Hertz.
    - sampling_rate (int): The sampling rate of the audio signal.

    Returns:
    - filtered_signal (numpy array): The filtered audio signal.
    """

    # Design the filter
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff_frequency / nyquist

    if key == 'lowpass':
        b, a = butter(6, normal_cutoff, btype='low', analog=False)
    elif key == 'highpass':
        b, a = butter(6, normal_cutoff, btype='high', analog=False)
    else:
        raise ValueError("Invalid filter type. Use 'lowpass' or 'highpass'.")

    # Apply the filter to the signal
    filtered_signal = filtfilt(b, a, input_signal)

    return filtered_signal

# Example usage:
# Load an example audio signal
audio_file = 'output.wav'
input_signal, sampling_rate = sf.read(audio_file)

# Choose filter type based on the key variable
key_variable = 'highpass'  # Change this to 'lowpass' if you want a low-pass filter

# Apply the filter
filtered_signal = apply_audio_filter(input_signal, key_variable)

# Export the filtered audio to a new file
output_file = f'filtered_{key_variable}_output.wav'
sf.write(output_file, filtered_signal, sampling_rate)

