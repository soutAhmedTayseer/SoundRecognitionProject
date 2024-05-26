# import numpy as np
# from scipy.signal import butter, filtfilt
# import soundfile as sf

# def apply_audio_filter(input_signal, key, cutoff_frequency=1000, band_width=None, sampling_rate=44100, filter_order=6):
#     """
#     Apply a low-pass, high-pass, band-pass, or band-stop filter to an input audio signal.

#     Parameters:
#     - input_signal (numpy array): The input audio signal.
#     - key (str): The key variable to select the filter ('lowpass', 'highpass', 'bandpass', or 'bandstop').
#     - cutoff_frequency (float): The cutoff frequency for low-pass and high-pass filters, or the center frequency for band-pass and band-stop filters, in Hertz.
#     - band_width (float, optional): The bandwidth of the band-pass or band-stop filter in Hertz. Required for 'bandpass' and 'bandstop' filters, ignored for 'lowpass' and 'highpass'.
#     - sampling_rate (int): The sampling rate of the audio signal.
#     - filter_order (int): The order of the Butterworth filter.

#     Returns:
#     - filtered_signal (numpy array): The filtered audio signal.
#     """

#     # Design the filter
#     nyquist = 0.5 * sampling_rate
#     normal_cutoff = cutoff_frequency / nyquist

#     if key == 'lowpass':
#         b, a = butter(filter_order, normal_cutoff, btype='low', analog=False)
#     elif key == 'highpass':
#         b, a = butter(filter_order, normal_cutoff, btype='high', analog=False)
#     elif key == 'bandpass':
#         if band_width is None:
#             raise ValueError("Bandwidth must be specified for 'bandpass' filter.")
#         low = (cutoff_frequency - 0.5 * band_width) / nyquist
#         high = (cutoff_frequency + 0.5 * band_width) / nyquist
#         b, a = butter(filter_order, [low, high], btype='band', analog=False)
#     elif key == 'bandstop':
#         if band_width is None:
#             raise ValueError("Bandwidth must be specified for 'bandstop' filter.")
#         low = (cutoff_frequency - 0.5 * band_width) / nyquist
#         high = (cutoff_frequency + 0.5 * band_width) / nyquist
#         b, a = butter(filter_order, [low, high], btype='bandstop', analog=False)
#     else:
#         raise ValueError("Invalid filter type. Use 'lowpass', 'highpass', 'bandpass', or 'bandstop'.")

#     # Apply the filter to the signal
#     filtered_signal = filtfilt(b, a, input_signal)

#     return filtered_signal

# # Example usage:
# # Load an example audio signal
# audio_file = 'output.wav'
# input_signal, sampling_rate = sf.read(audio_file)

# # Choose filter type based on the key variable
# key_variable = 'bandstop'  # Change this to 'bandstop', 'lowpass', or 'highpass' as needed

# # Adjust the filter parameters to feel the impact
# cutoff_frequency = 1000     # Adjust this to change the cutoff frequency or center frequency
# band_width = 500            # Adjust this to change the bandwidth (required for 'bandpass' and 'bandstop')

# # Apply the filter
# filtered_signal = apply_audio_filter(input_signal, key_variable, cutoff_frequency, band_width, sampling_rate)

# # Export the filtered audio to a new file
# output_file = f'filtered_{key_variable}_{cutoff_frequency}Hz_bandwidth_{band_width}Hz.wav'
# sf.write(output_file, filtered_signal, sampling_rate)


import numpy as np
from scipy.signal import butter, filtfilt
import soundfile as sf

class AudioFilter:
    def __init__(self):
        pass

    def apply_filter(self, input_signal, key, cutoff_frequency=1000, band_width=None, sampling_rate=16000, filter_order=6):
        """
        Apply a low-pass, high-pass, band-pass, or band-stop filter to an input audio signal.

        Parameters:
        - input_signal (numpy array): The input audio signal.
        - key (str): The key variable to select the filter ('lowpass', 'highpass', 'bandpass', or 'bandstop').
        - cutoff_frequency (float): The cutoff frequency for low-pass and high-pass filters, or the center frequency for band-pass and band-stop filters, in Hertz.
        - band_width (float, optional): The bandwidth of the band-pass or band-stop filter in Hertz. Required for 'bandpass' and 'bandstop' filters, ignored for 'lowpass' and 'highpass'.
        - sampling_rate (int): The sampling rate of the audio signal.
        - filter_order (int): The order of the Butterworth filter.

        Returns:
        - filtered_signal (numpy array): The filtered audio signal.
        """

        # Design the filter
        nyquist = 0.5 * sampling_rate
        normal_cutoff = cutoff_frequency / nyquist

        if key == 'lp':
            b, a = butter(filter_order, normal_cutoff, btype='low', analog=False)
        elif key == 'hp':
            b, a = butter(filter_order, normal_cutoff, btype='high', analog=False)
        elif key == 'bp':
            if band_width is None:
                raise ValueError("Bandwidth must be specified for 'bandpass' filter.")
            low = (cutoff_frequency - 0.5 * band_width) / nyquist
            high = (cutoff_frequency + 0.5 * band_width) / nyquist
            b, a = butter(filter_order, [low, high], btype='band', analog=False)
        elif key == 'bs':
            if band_width is None:
                raise ValueError("Bandwidth must be specified for 'bandstop' filter.")
            low = (cutoff_frequency - 0.5 * band_width) / nyquist
            high = (cutoff_frequency + 0.5 * band_width) / nyquist
            b, a = butter(filter_order, [low, high], btype='bandstop', analog=False)
        else:
            raise ValueError("Invalid filter type. Use 'lowpass', 'highpass', 'bandpass', or 'bandstop'.")

        # Apply the filter to the signal
        filtered_signal = filtfilt(b, a, input_signal)

        return filtered_signal

if __name__ == "__main__":
    # Example usage within the main block
    audio_filter = AudioFilter()

    # Input filter parameters from the user
    key_variable = input("Enter filter type ('lp', 'hp', 'bp', or 'bs'): ")
    cutoff_frequency = float(input("Enter cutoff frequency in Hertz: "))
    band_width = None
    if key_variable in ['bp', 'bs']:
        band_width = float(input("Enter bandwidth in Hertz: "))

    # Load an example audio signal
    audio_file = 'new_out.wav'
    input_signal, sampling_rate = sf.read(audio_file)

    # Apply the filter
    filtered_signal = audio_filter.apply_filter(input_signal, key_variable, cutoff_frequency, band_width, sampling_rate)

    # Export the filtered audio to a new file
    output_file = f'filtered_{key_variable}.wav'
    sf.write(output_file, filtered_signal, sampling_rate)
