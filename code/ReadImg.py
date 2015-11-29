import numpy as np
import cv2
import cv

imgs = ['roomleft1.jpeg', 'scarlett.jpg', 'matlab.png']

for img in imgs:
    a = cv2.imread(img)
    print img
    print a
    try:
        plt.imshow(a,'gray')
        plt.show()
    except:
        print "Error", img
    print "*********"
