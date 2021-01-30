import pyaudio
import wave
import numpy
import matplotlib.pyplot as plt
import pickle

CHUNK = 1
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()


stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = numpy.frombuffer(stream.read(CHUNK),'Int16')
    time = (i * RECORD_SECONDS * CHUNK / RATE )
    frames.append([time,data])

print("* done recording")

print(data)

with open('amplitude','wb') as f:
    pickle.dump(frames,f)

stream.stop_stream()
stream.close()
p.terminate()



plt.plot(frames)
plt.show()
