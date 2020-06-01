# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:42:32 2020

@author: OGK
"""

import mahotas
import cv2
image = cv2.imread("manzara.jpg")
cv2.imshow("Original",image)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("imshow",image)

T=mahotas.thresholding.otsu(blurred)
print("otsu threshold: {}".format(T))
thresh = image.copy()
thresh[thresh>T]=255
thresh[thresh<255]=0
thresh=cv2.bitwise_not(thresh)
cv2.imshow("otsu",thresh)

T=mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}",format(T))
thresh=image.copy()
thresh[thresh>T]=255
thresh[thresh<255]=0
thresh=cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard",thresh)
cv2.waitKey(0)