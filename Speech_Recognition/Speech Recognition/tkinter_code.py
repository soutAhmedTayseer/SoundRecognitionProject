import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from threading import Thread
from ttkthemes import ThemedTk
import soundfile as sf
from SpeechRecorder import Recorder 
from SpeechFilter import AudioFilter
from SpeechRecognizer import Recognizer
import pygame
from PIL import Image, ImageTk

class AudioProcessingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Mixer")

        # Set style for ttk
        self.style = ttk.Style()
        self.style.theme_use("arc")  # You can experiment with different themes

        # Set colors
        self.root.configure(bg="#d6424c")  # Background color
        self.record_frame_color = "#8f1d24"  # Record frame background color
        self.filter_frame_color = "#E0E0E0"  # Filter frame background color
        self.button_color = "white"  # Button background color
        self.button_text_color = "black"  # Button text color

        # Create frames
        self.record_frame = ttk.Frame(root, padding="10", style="My.TFrame")
        self.record_frame.grid(row=0, column=0, padx=10, pady=10)

        self.filter_frame = ttk.Frame(root, padding="10", style="My.TFrame")
        self.filter_frame.grid(row=1, column=0, padx=10, pady=10)

        # Initialize variables
        self.recording_file_path = ""
        self.filtered_audio_file = ""

         #load Icons
        self.record_icon = self.load_icon("D:\\study\\sound\\Speech_Recognition\\Speech Recognition\\icons\\record_icon.png")
        self.play_icon = self.load_icon("D:\\study\\sound\\Speech_Recognition\\Speech Recognition\\icons\\play_icon.png")
        self.filter_icon = self.load_icon("D:\\study\\sound\\Speech_Recognition\\Speech Recognition\\icons\\filter_icon.png")

        # Record Button
        self.record_button = ttk.Button(
            self.record_frame,
            text="Record Audio",
            image=self.record_icon,
            compound=tk.LEFT,  # Combine text and image on left
            command=self.record_audio,
            style="My.TButton"
        )
        self.record_button.grid(row=0, column=0, padx=10, pady=10)

        # Playback Buttons
        self.play_recorded_button = ttk.Button(
            self.record_frame,
            text="Play Recorded Audio",
            image=self.play_icon,
            compound=tk.LEFT,
            command=self.play_recorded_audio,
            style="My.TButton"
        )
        self.play_recorded_button.grid(row=1, column=0, padx=10, pady=10)

        self.play_filtered_button = ttk.Button(
            self.filter_frame,
            text="Play Filtered Audio",
            image=self.filter_icon,
            compound=tk.LEFT,
            command=self.play_filtered_audio,
            style="My.TButton"
        )
        self.play_filtered_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Filter Parameters Entry
        self.filter_label = ttk.Label(
            self.filter_frame,
            text="Filter Type:",
            style="My.TLabel"
        )
        self.filter_label.grid(row=0, column=0, padx=10, pady=10)

        self.filter_choices = ["lp", "hp", "bp", "bs"]
        self.filter_combobox = ttk.Combobox(self.filter_frame, values=self.filter_choices, style="My.TCombobox")
        self.filter_combobox.set("bp")  # Set default value as bp
        self.filter_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.cutoff_label = ttk.Label(
            self.filter_frame,
            text="Cutoff Frequency (Hertz): ",
            style="My.TLabel"
        )
        self.cutoff_label.grid(row=1, column=0, padx=10, pady=10)
        self.cutoff_entry = ttk.Entry(self.filter_frame, style="My.TEntry")
        self.cutoff_entry.grid(row=1, column=1, padx=10, pady=10)

        self.bandwidth_label = ttk.Label(
            self.filter_frame,
            text="Bandwidth (Hertz): ",
            style="My.TLabel"
        )
        self.bandwidth_label.grid(row=2, column=0, padx=10, pady=10)
        self.bandwidth_entry = ttk.Entry(self.filter_frame, style="My.TEntry")
        self.bandwidth_entry.grid(row=2, column=1, padx=10, pady=10)

        # Apply Filter and Recognize button
        self.process_button = ttk.Button(
            self.filter_frame,
            text="Apply Filters and Recognize",
            command=self.process_audio,
            style="My.TButton"
        )
        self.process_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Test Recognition Button
        self.test_recognition_button = ttk.Button(
            self.filter_frame,
            text="Test Recognition Without Filters",
            command=self.test_recognition,
            style="My.TButton"
        )
        self.test_recognition_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Create custom styles
        self.style.configure("My.TFrame", background=self.filter_frame_color)
        self.style.configure("My.TLabel", background=self.filter_frame_color, foreground="#333333")  # Dark text color
        self.style.configure("My.TEntry", background=self.filter_frame_color)
        self.style.configure("My.TButton", background=self.button_color, foreground=self.button_text_color)
        self.style.configure("My.TCombobox", background=self.filter_frame_color)

    def load_icon(self, filename):
        # Load an image and create a PhotoImage object for Tkinter
        img = Image.open(filename)
        img = img.resize((25, 25))  # Resize if needed
        icon = ImageTk.PhotoImage(img)
        return icon    

    def record_audio(self):
        recorder = Recorder()
        recorded_frames = recorder.record()
        self.recording_file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Wave files", "*.wav")])
        recorder.stop_and_save(recorded_frames, output_file=self.recording_file_path)
        messagebox.showinfo("Info", "Audio recording completed and saved!")
         # Enable playback button after recording
        self.play_recorded_button['state'] = 'normal'


    def play_recorded_audio(self):
        if self.recording_file_path:
            pygame.mixer.init()
            pygame.mixer.music.load(self.recording_file_path)
            pygame.mixer.music.play()

    def process_audio(self):
        key_variable = self.filter_combobox.get().lower()
        cutoff_frequency = float(self.cutoff_entry.get())
        band_width = float(self.bandwidth_entry.get()) if key_variable in ['bp', 'bs'] else None

        audio_filter = AudioFilter()

        input_signal, sampling_rate = sf.read(self.recording_file_path)

        filtered_signal = audio_filter.apply_filter(input_signal, key_variable, cutoff_frequency, band_width, sampling_rate)

        self.filtered_audio_file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Wave files", "*.wav")])
        sf.write(self.filtered_audio_file, filtered_signal, sampling_rate)
        messagebox.showinfo("Info", "Audio filtering completed and saved!")

        # Enable playback button after processing
        self.play_filtered_button['state'] = 'normal'

        # Start recognition in a separate thread to prevent GUI freezing
        recognition_thread = Thread(target=self.recognize_audio)
        recognition_thread.start()


    def play_filtered_audio(self):
        if self.filtered_audio_file:
            pygame.mixer.init()
            pygame.mixer.music.load(self.filtered_audio_file)
            pygame.mixer.music.play()

    def recognize_audio(self):
        my_recognizer = Recognizer()
        try:
            my_recognizer.recognize_and_print(self.filtered_audio_file)
            messagebox.showinfo("Info", "Speech recognition completed!")
        except Exception as e:
            messagebox.showerror("Error", f"Error in speech recognition: {e}")

    def test_recognition(self):
        my_recognizer = Recognizer()
        try:
            my_recognizer.recognize_and_print(self.recording_file_path)
            messagebox.showinfo("Info", "Speech recognition without filters completed!")
        except Exception as e:
            messagebox.showerror("Error", f"Error in speech recognition: {e}")

if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = AudioProcessingGUI(root)
    root.mainloop()