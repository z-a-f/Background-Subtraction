#!/usr/bin/env python

import numpy as np
import cv2
import matplotlib.pyplot as plt

SHIFT = 2**4
MOD = 2**16

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
frame = cv2.resize(frame, None, fx = 0.25, fy = 0.25, interpolation = cv2.INTER_CUBIC)

bg = frame[:,:]
mod = lambda a,b: (a - (a/b) * b)
while(True):
	ret, frame = cap.read()
	frame = cv2.resize(frame, None, fx = 0.25, fy = 0.25, interpolation = cv2.INTER_CUBIC)
	# channels = cv2.split(frame)
	
	# for idx in xrange(1):
	bg = bg - (bg / SHIFT) + frame  # channels[idx]
	#~ plt.imshow(frame)
	
	#frame_merge = cv2.merge(bg)
	# print len(np.array(bg % MOD)), len(frame)
	cv2.imshow('FG', np.abs(frame - bg))
	frame = cv2.hconcat((frame, bg/SHIFT))
	cv2.imshow('frame',frame)
	#~ cv2.imshow('frame merged', frame_merge)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
