# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import cv2
import matplotlib.pyplot as plt


img=cv2.imread("swapnil.jpeg")
"""
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img)
plt.axis(False)
plt.show()

plt.imshow(img[:,:,::-1])
plt.axis(False)
plt.show()

RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.axis(False)
plt.show()

"""

grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert_img=cv2.bitwise_not(grey_img)
#invert_img=255-grey_img


blur_img=cv2.GaussianBlur(invert_img, (111,111),0)


invblur_img=cv2.bitwise_not(blur_img)
#invblur_img=255-blur_img

sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

cv2.imwrite('sketch.png', sketch_img)

cv2.imshow('sketch image',sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()