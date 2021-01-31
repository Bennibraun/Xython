import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
import pickle

def freq_to_char(max_freq):
    freqs = [[0,2150],[2150,2400],[2400,2650],[2650,2850],[2850,3100],[3100,3400],
            [3400,3550],[3550,5000]]

    chars = ['C','D','E','F','G','A','B','K']

    for i, (min_f,max_f) in enumerate(freqs):
        if max_freq > min_f and max_freq <= max_f:
            return(chars[i])

filename = 'amplitude'

with open(filename, 'rb') as f:
     frames = pickle.load(f)


time,amplitude = map(list, zip(*frames))
amplitude = [amp[0] for amp in amplitude]

amplitude = amplitude

freqs,powers = scipy.signal.welch(amplitude,fs = 44100,nperseg=1000)



plt.plot(freqs,powers)
plt.xlim([0,5000])
#plt.show()
maxfreq = freqs[np.argmax(powers)]
symbol = freq_to_char(maxfreq)
print(symbol)
