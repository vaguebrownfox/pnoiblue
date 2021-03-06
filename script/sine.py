import numpy as np
from scipy.io import wavfile

sampleRate = 16000
frequency = 440
length = 12

t = np.linspace(0, length, sampleRate * length)  #  Produces a 5 second Audio-File
y = np.sin(frequency * 2 * np.pi * t)  #  Has frequency of 440Hz

wavfile.write('Sine.wav', sampleRate, y)

