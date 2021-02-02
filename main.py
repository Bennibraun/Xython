from amplitudeProcessing import freqHandler
from liveaudio import streamHandler
from xython import xylophuck
from config import *

if __name__ == __main__

audioHandler = streamHandler(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                io=True,
                chunk=CHUNK)

freqDomain = freqHandler()
