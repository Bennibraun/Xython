import scipy.signal
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pyaudio

filename = 'amplitude'

with open(filename, 'rb') as f:
     frames = pickle.load(f)


time,amplitude = map(list, zip(*frames))
amplitude = [amp[0] for amp in amplitude]

amplitude = amplitude[0:5000]

welched = scipy.signal.welch(amplitude)
# print(welched[0])

s = welched[1]
t = np.arange(0,5000,5000/len(s))

print("peak freq:",t[np.argmax(s)])

# plot time signal:
fig = plt.subplot()
fig.plot(t, s, color='C0')
fig.set_xlabel("Frequency")
fig.set_ylabel("Amplitude")

plt.show()