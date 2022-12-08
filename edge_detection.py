import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('yoda.jpeg',0)

plt.subplot(1,3,1)

plt.imshow(img)

plt.title('the image')

edges = cv.Canny(img,100,200)

plt.subplot(1,3,2)

plt.imshow(img,cmap = 'gray')

plt.title('Original Image')

plt.subplot(1,3,3)

plt.imshow(edges,cmap = 'gray')

plt.title('Edge Image')

plt.show()
