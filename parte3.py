#required libraries
from urllib.request import urlretrieve
import scipy.io.wavfile
import pydub
from numpy import fft as fft
import matplotlib.pyplot as plt

#a temp folder for downloads
temp_folder="/Users/LMI/Documents/PDI/"

rate,audData=scipy.io.wavfile.read(temp_folder+"audio.wav")

print(rate)     #Samples per seconds of the signal
print(audData)  #Data of the signal

print(audData.shape[0] / rate) #length of the signal

channel1 = audData[:,0]     #channel of the left
channel2 = audData[:,1]     #channel of the right

fourier = fft.fft(audData)

plt.plot(fourier, color='#ff7f00')
plt.xlabel('K')
plt.ylabel('Amplitude')


