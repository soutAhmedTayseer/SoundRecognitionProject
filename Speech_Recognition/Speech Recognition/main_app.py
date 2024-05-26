from SpeechRecorder import Recorder 
from SpeechFilter import AudioFilter
from SpeechRecognizer import Recognizer
from scipy.signal import butter, filtfilt
import soundfile as sf


if __name__ == "__main__":
    # record the audio 
    print('Step1: Recording audio...............')
    recorder = Recorder()
    recorded_frames = recorder.record()
    recording_file_path='new_out.wav'
    recorder.stop_and_save(recorded_frames,output_file=recording_file_path)

    print('Step2: Applying filters.........')
    audio_filter = AudioFilter()

    # Input filter parameters from the user
    key_variable = input("Enter filter type ('lowpass', 'highpass', 'bandpass', or 'bandstop'): ")
    cutoff_frequency = float(input("Enter cutoff frequency in Hertz: "))
    band_width = None
    if key_variable in ['bandpass', 'bandstop']:
        band_width = float(input("Enter bandwidth in Hertz: "))

    
   
    input_signal, sampling_rate = sf.read(recording_file_path)

    # Apply the filter
    filtered_signal = audio_filter.apply_filter(input_signal, key_variable, cutoff_frequency, band_width, sampling_rate)

    # Export the filtered audio to a new file
    filtered_audio_file = f'filtered_{key_variable}.wav'
    sf.write(filtered_audio_file, filtered_signal, sampling_rate)

    # the recognizer part 
    print('Step3: Applying the recognition......')
    my_recognizer = Recognizer()
    my_recognizer.recognize_and_print(filtered_audio_file)
