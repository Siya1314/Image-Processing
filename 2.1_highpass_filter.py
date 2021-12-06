# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:35:58 2021

@author: siyab
"""
import numpy as np
from skimage import io
from math import sqrt
import matplotlib.pyplot as plt

# read the image
img = io.imread('imgs/zoneplate.tif')

# define the distance
def distance(u,v):
    D = sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2)
    return D

#define the butterworth highpass filter
def butterworth_highpass(D0, imgShape, n):
    H = np.zeros(imgShape[:2])
    r, c = imgShape[:2]
    center = (r/2,c/2)
    for j in range(c):
        for i in range(r):
            D = distance((i, j), center)
            H[i, j] = 1-(1/(1+(D/D0)**(2*n)))
    return H

# we use the fast fourier transform to obtain the desired output.
f = np.fft.fft2(img)                #fast fourier transform
f_shift = np.fft.fftshift(f)        #shift to the center

Highpass_shift = f_shift*butterworth_highpass(45, img.shape, 3)
Highpass = np.fft.ifftshift(Highpass_shift)

Inverse_highpass = np.fft.ifft2(Highpass) #Inverse fast fourier transform

plt.imshow(np.abs(Inverse_highpass), cmap='gray')