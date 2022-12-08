import numpy as np

import cv2 as cv

from matplotlib import pyplot as plt

img = cv.imread('eye.jpg')

kernel = np.ones((5,5),np.float32)/25

'''
------------------------------------edge detection kernel--------------
kernel2 = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])
'''

dst = cv.filter2D(img,-1,kernel)


plt.subplot(121),plt.imshow(img),plt.title('Original')

plt.subplot(122),plt.imshow(dst),plt.title('Averaging')

plt.show()
