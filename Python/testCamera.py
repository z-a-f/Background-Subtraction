#!/usr/bin/env python

import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
ret, frame = cap.read(-1)

bg = [[[0] * len(frame[0]) for _ in xrange(len(frame))] for _ in xrange(3)]

while(True):
	ret, frame = cap.read()
	frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

	channels = cv2.split(frame)
	frame_merge = cv2.merge(channels)
	# for idx in xrange(3):
	#	bg[idx] = 
	#~ plt.imshow(frame)
	frame = cv2.hconcat((frame, frame_merge))
	cv2.imshow('frame',frame)
	#~ cv2.imshow('frame merged', frame_merge)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
