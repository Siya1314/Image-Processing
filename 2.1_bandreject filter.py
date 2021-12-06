# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:01:18 2021

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

# define the bandreject filter form of the butterworth
def butterworth_bandreject(D0, imgShape, n, W):  
    H = np.zeros(imgShape[:2])
    r, c = imgShape[:2]
    center = (r/2, c/2)
    for i in range(c):
        for j in range(r):
            D = distance((i, j), center)
            H[i, j] = 1/(1+(W*D)/((D**2) - (D0**2))**2*n)
    return H
# we use the fast fourier method to display the output
f = np.fft.fft2(img)              #fast fourier transform
f_shift = np.fft.fftshift(f)     # shift to center

bandreject_center = f_shift * butterworth_bandreject(30, img.shape, 50, 96)
bandreject = np.fft.ifftshift(bandreject_center)

Inverse_bandreject = np.fft.ifft2(bandreject)  #inverse fast fourier transform

plt.imshow(np.abs(Inverse_bandreject), cmap='gray')