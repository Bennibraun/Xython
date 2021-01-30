import scipy.signal
import pickle

filename = 'amplitude'

with open(filename, 'rb') as f:
     frames = pickle.load(f)


time,amplitude = map(list, zip(*frames))
amplitude = [amp[0] for amp in amplitude]

amplitude = amplitude[0:5000]

welched = scipy.signal.welch(amplitude)
print(welched)
