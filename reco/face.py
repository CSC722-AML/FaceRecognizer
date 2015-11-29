from __future__ import print_function, division
import sys, os
sys.dont_write_bytecode = True
import numpy as np
import cv2
__author__ = 'panzer'

HAAR_PATH = "haarcascades/"

face_cascade = cv2.CascadeClassifier(HAAR_PATH + 'haarcascade_frontalface_default.xml')
img = cv2.imread('yalefaces_jpgs/subject01.jpg')


sift = cv2.SIFT()
faces = face_cascade.detectMultiScale(img)

kp = sift.detect(img, None)

img2 = cv2.drawKeypoints(img, kp)

cv2.imwrite('sift_keypoints.jpg',img2)


