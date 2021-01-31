import pyaudio
import wave
import numpy
import matplotlib.pyplot as plt
import pickle

class streamHandler():
    def __init__(self,format=pyaudio.paInt16,channels=1,rate=44100,io=True,chunk=1):
        self.p = pyaudio.PyAudio()
        self.format = format
        self.channels = channels
        self.rate = rate
        self.io = io
        self.chunk = chunk

    def open_stream(self):

        self.stream = self.p.open(format=self.format,
                channels=self.channels,
                rate=self.rate,
                input=self.io,
                frames_per_buffer=self.chunk)

    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def record(self,stop_time):
        frames = []

        for i in range(0, int(self.rate / self.chunk * stop_time)):
            data = numpy.frombuffer(self.stream.read(self.chunk),'Int16')
            frames.append(data)

        return frames


CHUNK = 1
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'output'


audioHandler = streamHandler(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                io=True,
                chunk=CHUNK)

print("* recording")

audioHandler.open_stream()

frames = audioHandler.record(RECORD_SECONDS)

audioHandler.close_stream()

print("* done recording")

with open('amplitude','wb') as f:
    pickle.dump(frames,f)

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audioHandler.p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

#plt.plot(frames)
#plt.show()
