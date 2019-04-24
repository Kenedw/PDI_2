#required libraries
import scipy.io.wavfile
import pydub
from numpy import fft as fft 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2 

#a temp folder for downloads
temp_folder="/Users/LMI/Documents/PDI/"

rate,audData=scipy.io.wavfile.read(temp_folder+"audio.wav")

print(rate)     #Samples per seconds of the signal
print(audData)  #Data of the signal

print(audData.shape[0] / rate ) #length of the signal

length = audData.shape[0] // rate #length of the audio signal

#channel1 = audData[:,0]     #channel of the left
#channel2 = audData[:,1]     #channel of the right

four = fft.fft(audData)
#four.astype('complex')

plt.plot(four.real)
plt.xlabel('K')
plt.ylabel('Amplitude')
plt.show()

four = four[0:(length//2)]
#four = four/float(length)

#Calculates the frequency at each point in Hz
each_freq = np.arange(0, (length/2), 1.0) * (rate)

plt2.plot(each_freq/1000, 10*np.log10(four.real))
plt2.xlabel("Frequencia (kHz)")
plt2.ylabel("Potência (dB)")
plt2.show()



    
    

