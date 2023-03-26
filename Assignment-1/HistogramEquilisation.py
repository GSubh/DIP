# import Libraries
import cv2
import numpy as np

# read a image using imread
Lenna = cv2.imread('test_img2.png', 0)

# creating a Histograms Equalization
# # of a image using cv2.equalizeHist()
a = cv2.equalizeHist(Lenna)

# stacking images side-by-side
x = np.hstack((Lenna, a))

# show image input vs output
cv2.imshow('Equalised', x)

cv2.waitKey(0)
cv2.destroyAllWindows()
