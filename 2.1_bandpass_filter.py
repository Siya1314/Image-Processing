# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:01:58 2021

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

# define the butterworth bandreject filter
def butterworth_bandreject(D0, imgShape, n, W):  
    H = np.zeros(imgShape[:2])
    r, c = imgShape[:2]
    center = (r/2, c/2)
    for i in range(c):
        for j in range(r):
            D = distance((i, j), center)
            H[i, j] = 1/(1+(W*D)/((D**2) - (D0**2))**2*n)
    return H

# generating bandpass image from bandworth_bandreject
bandpass = 1 - butterworth_bandreject(30, img.shape, 3, 300)
f = np.fft.fft2(img)
f_shift = np.fft.fftshift(f)

bandpass_center = f_shift * bandpass
bandpass = np.fft.ifftshift(bandpass_center)
inverse_bandpass = np.fft.ifft2(bandpass)
plt.imshow(np.abs(inverse_bandpass), 'gray')
