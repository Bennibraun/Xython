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

time,amplitude = map(list, zip(*frames))

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(amplitude))
wf.close()

#plt.plot(frames)
#plt.show()
