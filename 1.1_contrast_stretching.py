# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:46:58 2021

@author: siyab
"""

#contrast sketching
import numpy as np
from skimage import io, img_as_float
import matplotlib.pyplot as plt

# read images and save them as as float for our defined function
img1 = img_as_float(io.imread('imgs/road_low_1.jpg'))
img2 = img_as_float(io.imread('imgs/road_low_2.jpg'))
img3 = img_as_float(io.imread('imgs/sports_low.png'))

# we define contrast sketching 
def contrast_stretching(image, N):
    L = 2**N                     # N is the bit size
    old_image = image
    row, column = image.shape
    for i in range(row):
        for j in range(column):
            r, r_min = image[i, j], np.min(old_image)
            r_max = np.max(old_image)
            image[i, j] = ((L - 1)*(r - r_min))/(r_max - r_min)
    return image

contrast_img1 = contrast_stretching(img1, 8)
contrast_img2 = contrast_stretching(img2, 8)
contrast_img3 = contrast_stretching(img3, 8)

print('For road_low_1')
plt.figure(figsize=(15, 10))

plt.subplot(231)
plt.imshow(img1, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('original')

plt.subplot(232)
plt.hist(img1.ravel(), bins=256)
plt.title('original histogram')

plt.subplot(234)
plt.imshow(contrast_img1, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('modified')

plt.subplot(235)
plt.hist(contrast_img1.ravel(), bins=256)
plt.title('modified histogram')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0, right=1)

print('For road_low_2')
plt.figure(figsize=(15, 10))

plt.subplot(231)
plt.imshow(img2, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('original')

plt.subplot(232)
plt.hist(img2.ravel(), bins=256)
plt.title('original histogram')

plt.subplot(234)
plt.imshow(contrast_img2, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('modified')

plt.subplot(235)
plt.hist(contrast_img2.ravel(), bins=256)
plt.title('modified histogram')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0, right=1)


print('For sports_low')

plt.figure(figsize=(15, 10))

plt.subplot(231)
plt.imshow(img3, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('original')

plt.subplot(232)
plt.hist(img3.ravel(), bins=256)
plt.title('original histogram')

plt.subplot(234)
plt.imshow(contrast_img3, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('modified')

plt.subplot(235)
plt.hist(contrast_img3.ravel(), bins=256)
plt.title('modified histogram')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0, right=1)