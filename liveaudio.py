import pyaudio
import wave
import numpy
import matplotlib.pyplot as plt
import pickle
import threading
from tkinter import *
from amplitudeProcessing import frames_to_char


class streamHandler():
    def __init__(self,format=pyaudio.paInt16,channels=1,rate=44100,io=True,chunk=1):
        self.p = pyaudio.PyAudio()
        self.format = format
        self.channels = channels
        self.rate = rate
        self.io = io
        self.chunk = chunk

        self.open = False

    def open_stream(self):

        self.stream = self.p.open(format=self.format,
                channels=self.channels,
                rate=self.rate,
                input=self.io,
                frames_per_buffer=self.chunk)

        self.open = True

    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        self.open = False

    def record(self,stop_time):
        frames = []

        for i in range(0, int(self.rate / self.chunk * stop_time)):
<<<<<<< HEAD
            try:
                data = numpy.frombuffer(self.stream.read(self.chunk),'Int16')
                frames.append(data)
            except:
                # print('failed to retrieve data from audio buffer')
                break
=======
            data = numpy.frombuffer(self.stream.read(self.chunk,exception_on_overflow=False),'Int16')
            frames.append(data)
>>>>>>> 63b31611491f72c8cc38827e837e83591cd25ab9

        frames = [amp[0] for amp in frames]

        return frames


CHUNK = 1
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
<<<<<<< HEAD
RECORD_SECONDS = 1
=======
RECORD_SECONDS = 2
>>>>>>> 63b31611491f72c8cc38827e837e83591cd25ab9
WAVE_OUTPUT_FILENAME = 'output'

program_text = 'test'
frames = 'frame'
recording_active = True
end_program = False
pause_btn = None
resume_btn = None
end_btn = None

<<<<<<< HEAD
audioHandler = streamHandler(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                io=True,
                chunk=CHUNK)

def resume_recording():
    print('resume')
    global resume_btn
    global pause_btn
    global recording_active
    global audioHandler
    recording_active = True
    resume_btn.place_forget()
    pause_btn = Button(window, text="Pause", command=pause_recording, height=3, width=15)
    pause_btn.place(x=20, y=30)
    audioHandler.open_stream()

def pause_recording():
    print('pause')
    global resume_btn
    global pause_btn
    global recording_active
    recording_active = False
    pause_btn.place_forget()
    resume_btn = Button(window, text="Resume", command=resume_recording, height=3, width=15)
    resume_btn.place(x=20, y=30)

def end_listening():
    print('ending listener')
    global pause_btn
    global resume_btn
    global end_program
    end_program = True

def start_threading():
    global end_btn
    global pause_btn
    start_btn.place_forget()
    pause_btn = Button(window, text="Pause", command=pause_recording, height=3, width=15)
    pause_btn.place(x=20, y=30)
    end_btn = Button(window, text="End", command=end_listening, height=3, width=15)
    end_btn.place(x=20, y=100)
    t2 = threading.Thread(target=gather_live_audio)
    t2.start()

def process_audio():
    print('processing audio')
    global frames
    note = frames_to_char(frames)
    print(frames[:20])
    if note:
        print(note)
        program_text += note


def gather_live_audio():
    global recording_active
    global frames
    print("beginning recording")

    audioHandler.open_stream()

    T = Text(window, height=10, width=40)
    T.place(x=150,y=10)

    while True:
        if recording_active:
            print('recording sound')
            frames = audioHandler.record(RECORD_SECONDS)
            print(len(frames))
            t1 = threading.Thread(target=process_audio)
            t1.start()
            # lbl = Label(window, text=program_text)
            # lbl.grid(column=0, row=0)
            T.delete('1.0', END)
            T.insert(END, program_text)
        if end_program:
            break

    print('ending recording, closing stream')
    audioHandler.close_stream()

window = Tk()
window.title("Xython Interpreter")
window_width = 500
window_height = 200
window.geometry(str(window_width)+'x'+str(window_height))
start_btn = Button(window, text="Start Listening", command=start_threading, height=3, width=15)
start_btn.place(x=20, y=30)
window.mainloop()

print("* done recording")

with open('amplitude','wb') as f:
    pickle.dump(frames,f)

# print(frames)

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audioHandler.p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
=======

# audioHandler = streamHandler(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 io=True,
#                 chunk=CHUNK)
#
# print("* recording")
#
# audioHandler.open_stream()
#
# frames = audioHandler.record(RECORD_SECONDS)
#
# audioHandler.close_stream()
#
# print("* done recording")
#
# with open('amplitude','wb') as f:
#     pickle.dump(frames,f)
#
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(audioHandler.p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(amplitude))
# wf.close()
>>>>>>> 63b31611491f72c8cc38827e837e83591cd25ab9

#plt.plot(frames)
#plt.show()
