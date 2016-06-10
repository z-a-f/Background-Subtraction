#!/usr/bin/env python

import numpy as np
import cv2
import matplotlib.pyplot as plt

SHIFT = 2**4
MOD = 2**16

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
frame = cv2.resize(frame, None, fx = 0.25, fy = 0.25, interpolation = cv2.INTER_CUBIC)
k = 1.
fact =  1 / k
thresh = 15
f = np.vectorize(lambda x: 	255*(abs(x) > thresh))


bg = frame[:,:]
mod = lambda a,b: (a - (a/b) * b)
while(True):
	ret, frame = cap.read()
	frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

	bg = bg - bg * fact + frame
	frame_bg = bg.astype(int)
	frame_fg = f(frame_bg - frame)

	cv2.imshow('frame',frame)
	cv2.imshow('bg', frame_bg)
	cv2.imshow('fg', frame_fg)
	#~ cv2.imshow('frame merged', frame_merge)
	key = cv2.waitKey(30) & 0xff
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()
