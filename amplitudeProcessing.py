import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
import pickle
from liveaudio import *

class freqHandler():

    def __init__(self,min_freq=1000,max_freq=5000):
        self.min_freq = min_freq
        self.max_freq = max_freq

        self.freqs = [[1800,2150],[2150,2400],[2400,2600],[2600,2850],[2850,3200],[3200,3400],
                [3400,3575],[3575,5000]]

<<<<<<< HEAD
def frames_to_char(frames):
    try:
        time,amplitude = map(list, zip(*frames))
        amplitude = [amp[0] for amp in amplitude]
        freqs,powers = scipy.signal.welch(amplitude,fs = 44100,nperseg=1000)
        maxfreq = freqs[np.argmax(powers)]
        return freq_to_char(maxfreq)
    except:
        print('frames_to_char failed, ',len(frames))

# filename = 'amplitude'

# with open(filename, 'rb') as f:
#      frames = pickle.load(f)


# time,amplitude = map(list, zip(*frames))
# amplitude = [amp[0] for amp in amplitude]

# amplitude = amplitude

# freqs,powers = scipy.signal.welch(amplitude,fs = 44100,nperseg=1000)


# plt.plot(freqs,powers)
# plt.xlim([0,5000])
# #plt.show()
# maxfreq = freqs[np.argmax(powers)]
# symbol = freq_to_char(maxfreq)
# print(maxfreq,symbol)
=======
        self.chars = ['C1','D','E','F','G','A','B','C2']

    def freq_to_char(self,max_freq):

        if max_freq < self.min_freq: return None

        for i, (min_f,max_f) in enumerate(self.freqs):
            if max_freq > min_f and max_freq <= max_f:
                return(chars[i])

    def get_max_strength_freq(self,time_data,plot=False):
        freqs,powers = scipy.signal.welch(time_data,fs = 44100,nperseg=1000)

        maxfreq = freqs[np.argmax(powers)]

        if plot:
            plt.plot(freqs,powers)
            plt.xlim([0,5000])
            plt.show()

        return maxfreq

    def retune(self,audioHandler,capture_secs=5):

        if audioHandler.open == False:
            audioHandler.open_stream()

        freqs = []
        for i in range(len(self.chars)):

            print('Please play note number #%d' % (i+1))
            frames = audioHandler.record(4)
            print('Recorded! Processing: . . .')
            maxfreq = self.get_max_strength_freq(frames)
            freqs.append(maxfreq)


        new_freqs = []
        for i in range(len(freqs)-1):
            new_freqs.append(np.mean((freqs[i],freqs[i+1])))
        freqs = new_freqs

        new_ranges = []
        for i in range(len(freqs)):
            if i == 0:
                new_ranges.append([self.min_freq,freqs[0]])
            elif i == len(freqs)-1:
                new_ranges.append([freqs[-1],self.max_freq])
            else:
                new_ranges.append([freqs[i],freqs[i+1]])

        self.freqs = new_ranges







audioHandler = streamHandler(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                io=True,
                chunk=CHUNK)

print("* recording")

audioHandler.open_stream()

frames = audioHandler.record(RECORD_SECONDS)

print("* done recording")

freqDomain = freqHandler()

freqDomain.retune(audioHandler)

amplitude = frames

maxfreq = freqDomain.get_max_strength_freq(amplitude,plot=True)
symbol = freqDomain.freq_to_char(maxfreq)
print(maxfreq,symbol)

audioHandler.close_stream()
>>>>>>> 63b31611491f72c8cc38827e837e83591cd25ab9
