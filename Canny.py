# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:42:32 2020

@author: OGK
"""

import numpy as np
import cv2
image = cv2.imread("sakiz.jpg")

cv2.imshow("Original",image)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Canny fonksiyonunu
canny= cv2.Canny(image,30,150)
cv2.imshow("Canny",canny)
cv2.waitKey(0)

#Görüntümüze Mean Adaptive Thresh uyguluyoruz.
thresh1=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,4)

#Görüntümüze Gaussian Adaptive Thresh uyguluyoruz.
thresh2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,6)

#Görüntülerimize Canny fonksiyonları uyguluyoruz.
canny1= cv2.Canny(thresh1,30,150)
cv2.imshow("Canny1",canny1)

canny2= cv2.Canny(thresh2,30,150)
cv2.imshow("Canny2",canny2)
cv2.waitKey(0)
