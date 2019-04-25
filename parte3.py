#required libraries
import scipy.io.wavfile
from numpy import fft as fft 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2 

import numpy
import numpy.fft
from numpy import *

import scipy
from scipy.fftpack import *

# Discrete Cosine Transforms (DCT)
def dct(vector):
  result = []
  factor = math.pi / len(vector)
  for i in range(len(vector)):
    soma = 0.0
    for (j, val) in enumerate(vector):
      soma += val * math.cos((j + 0.5) * i * factor)
    result.append(soma)
  return result

def idct(vector):
  result = []
  factor = math.pi / len(vector)
  for i in range(len(vector)):
    soma = vector[0] / 2.0
    for j in range(1, len(vector)):
      soma += vector[j] * math.cos(j * (i + 0.5) * factor)
    result.append(soma)
    return result

#a temp folder for downloads
temp_folder="/Users/LMI/Documents/PDI/"

rate,audData=scipy.io.wavfile.read(temp_folder+"a.wav")

print(rate)     #Samples per seconds of the signal
print(audData)  #Data of the signal

length = len(audData) #length of the audio signal

channel1 = audData[:,0]     #channel of the left
channel2 = audData[:,1]     #channel of the right

#aplica DCT
four = dct(channel1)

plt.figure(1)
plt.plot(four)


#desloca
x = 500
audishift1 = roll(four,x)
#audishift2 = roll(channel2,x)

if(x>0 and x<rate):
  for i in range(x):
    print(i)
    audishift1[i] = 0
    #audishift2[i] = 0

print(audishift1)
plt.figure(2)
plt.plot(audishift1)
plt2.show()

