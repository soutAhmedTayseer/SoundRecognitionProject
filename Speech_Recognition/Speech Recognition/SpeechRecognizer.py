# audio_file = sr.AudioFile("filtered_bandstop_1000Hz_bandwidth_500Hz.wav")
# #print(type(audio_file))
# recognizer= sr.Recognizer()
# recognizer.energy_threshold=600

# with audio_file as source:
#     #for noisy audio files 
#     recognizer.adjust_for_ambient_noise(source, duration=0.5)
#     audio_file_data= recognizer.record(source)
# print(type(audio_file_data))
# text= recognizer.recognize_google(audio_data=audio_file_data, language="en-US")
# print(text)

import speech_recognition as sr

class Recognizer():
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 100

    def recognize_audio_file(self, file_path):
        audio_file = sr.AudioFile(file_path)

        with audio_file as source:
            # For noisy audio files
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio_file_data = self.recognizer.record(source)

        return audio_file_data
    
    def recognize_and_print(self, file_path):
        try:
            audio_file_data = self.recognize_audio_file(file_path)
            text = self.recognizer.recognize_google(audio_data=audio_file_data, language="en-US")
            print("Recognized Text:", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    # Example usage:
    # file_path = "filtered_bandstop_1000Hz_bandwidth_500Hz.wav"
    file_path='filtered_hp.wav'
    my_recognizer = Recognizer()
    my_recognizer.recognize_and_print(file_path)
