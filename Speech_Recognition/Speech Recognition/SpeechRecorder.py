# import pyaudio
# import wave

# frames_per_buffer= 3200  # Record in buffer of 3200 samples
# format= pyaudio.paInt32 #32 bit per sample
# channels= 1
# sample_rate= 16000

# p= pyaudio.PyAudio() #pyaudio object
# stream= p.open(format= format, 
#                channels= channels,
#                rate= sample_rate,
#                input= True, #to capture audio
#                frames_per_buffer= frames_per_buffer)

# print("Start Recording")

# seconds=5 #record duration
# frames=[] # Initialize array to store frames

# # Store data in buffer for 3 seconds
# for i in range(0, int(sample_rate / frames_per_buffer * seconds)):
#     data = stream.read(frames_per_buffer)#read 3200 frame at each iteration
#     frames.append(data)

# print("Finished Recording")    

# stream.stop_stream()
# stream.close()
# # Terminate the PortAudio interface
# p.terminate()


# wf= wave.open("output.wav", "wb")
# wf.setnchannels(channels)
# wf.setsampwidth(p.get_sample_size(format))
# wf.setframerate(sample_rate)
# #write all frames in binary string, combine all frames into binary string .
# wf.writeframes(b''.join(frames))
# wf.close()

import pyaudio
import wave

class Recorder:
    def __init__(self, frames_per_buffer=3200, format=pyaudio.paInt32, channels=1, sample_rate=16000):
        self.frames_per_buffer = frames_per_buffer
        self.format = format
        self.channels = channels
        self.sample_rate = sample_rate
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=format,
            channels=channels,
            rate=sample_rate,
            input=True,
            frames_per_buffer=frames_per_buffer
        )

    def record(self, duration=5):
        print("Start Recording")
        frames = [] # Initialize array to store frames

        # Store data in buffer for the specified duration
        for i in range(0, int(self.sample_rate / self.frames_per_buffer * duration)):
            data = self.stream.read(self.frames_per_buffer)
            frames.append(data)

        print("Finished Recording")
        return frames

    def stop_and_save(self, frames, output_file="output.wav"):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(output_file, "wb")
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()

# Example usage:
if __name__ == "__main__":
    recorder = Recorder()
    recorded_frames = recorder.record()
    recorder.stop_and_save(recorded_frames,output_file='new_out.wav')
