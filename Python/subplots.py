#!/usr/bin/env python

import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.figure()
    img1 = plt.imread('../test_images/4.2.03.tiff')
    img2 = plt.imread('../test_images/4.2.04.tiff')
    plt.subplot(121), plt.imshow(img1), plt.title("Video Feed 1")
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img2), plt.title("Video Feed 2")
    plt.xticks([]), plt.yticks([])
    plt.show()