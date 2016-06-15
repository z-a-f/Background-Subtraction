#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('../test_images/house.tiff', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()
