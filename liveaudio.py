import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import pickle
import threading
from tkinter import *
from xython import xylophuck
import scipy.signal


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
            try:
                data = np.frombuffer(self.stream.read(self.chunk),'Int16')
                frames.append(data)
            except:
                # print('failed to retrieve data from audio buffer')
                break

        frames = [amp[0] for amp in frames]

        return frames


CHUNK = 1
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = 'output'

program_text = ''
frames = 'frame'
recording_active = True
end_program = False
pause_btn = None
resume_btn = None
end_btn = None
compile_btn = None

audioHandler = streamHandler(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                io=True,
                chunk=CHUNK)

freqs = [[1800,2150],[2150,2400],[2400,2600],[2600,2850],[2850,3200],[3200,3400],[3400,3575],[3575,5000]]
chars = ['C','D','E','F','G','A','B','K']


def get_max_strength_freq(time_data,plot=False):

    print('number of frames', len(time_data))

    freqs,powers = scipy.signal.welch(time_data,fs = 44100,nperseg=500)

    maxfreq = freqs[np.argmax(powers)]

    if plot:
        plt.plot(freqs,powers)
        plt.xlim([0,5000])
        plt.show()

    return maxfreq

def freq_to_char(time_data):

        max_freq = get_max_strength_freq(time_data)

        if max_freq < 1000: return None

        for i, (min_f,max_f) in enumerate(freqs):
            if max_freq > min_f and max_freq <= max_f:
                return(chars[i])



def compile_program():
    global program_text
    T = Text(window, height=5, width=40)
    T.place(x=150,y=80)
    try:
        output = xylophuck(program_text)
    except:
        print('xylophuck function call failed')
        output = 'Compilation error'
    if output == None or output == '':
        output = 'No output'
    T.insert(END, output)


def resume_recording():
    print('resume')
    global resume_btn
    global pause_btn
    global recording_active
    global audioHandler
    recording_active = True
    resume_btn.place_forget()
    pause_btn = Button(window, text="Pause", command=pause_recording, bg='blue', height=3, width=15)
    pause_btn.place(x=20, y=30)
    audioHandler.open_stream()

def pause_recording():
    print('pause')
    global resume_btn
    global pause_btn
    global recording_active
    recording_active = False
    pause_btn.place_forget()
    resume_btn = Button(window, text="Resume", command=resume_recording, bg='blue', height=3, width=15)
    resume_btn.place(x=20, y=30)

def end_listening():
    print('ending listener')
    global pause_btn
    global resume_btn
    global end_btn
    global end_program
    end_program = True
    try:
        pause_btn.place_forget()
    except:
        pass
    try:
        resume_btn.place_forget()
    except:
        pass
    end_btn.place_forget()
    compile_btn = Button(window, text="Compile and Run", command=compile_program, bg='yellow', height=3, width=15)
    compile_btn.place(x=20, y=100)

def start_threading():
    global end_btn
    global pause_btn
    start_btn.place_forget()
    pause_btn = Button(window, text="Pause", command=pause_recording, bg='blue', height=3, width=15)
    pause_btn.place(x=20, y=30)
    end_btn = Button(window, text="End", command=end_listening, bg='red', height=3, width=15)
    end_btn.place(x=20, y=100)
    t2 = threading.Thread(target=gather_live_audio)
    t2.start()

def process_audio():
    print('processing audio')
    global frames
    global program_text
    global chars
    note = freq_to_char(frames)
    print(frames[:20])
    if note:
        print('note',note)
        if note in chars:
            program_text += note

def gather_live_audio():
    global recording_active
    global frames
    global program_text
    print("beginning recording")

    T = Text(window, height=5, width=40)
    T.place(x=150,y=10)

    while True:
        if recording_active:
            print('recording sound')
            audioHandler.open_stream()
            frames = audioHandler.record(RECORD_SECONDS)
            t1 = threading.Thread(target=process_audio)
            t1.start()
            T.delete('1.0', END)
            T.insert(END, program_text)
        if end_program or not frames:
            break
        program_text = T.get('1.0',END)
        print('notes: ',program_text)


    print('ending recording, closing stream')
    audioHandler.close_stream()

window = Tk()
window.title("Xython Interpreter")
window_width = 500
window_height = 200
window.geometry(str(window_width)+'x'+str(window_height))
start_btn = Button(window, text="Start Listening", command=start_threading, bg='green', height=3, width=15)
start_btn.place(x=20, y=30)
window.mainloop()

print("* done recording")

with open('amplitude','wb') as f:
    pickle.dump(frames,f)

# print(frames)

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

#plt.plot(frames)
#plt.show()
