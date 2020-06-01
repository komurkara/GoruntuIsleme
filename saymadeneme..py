# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:42:32 2020

@author: OGK
"""

import numpy as np
import cv2

image = cv2.imread("p.jpg")
#cv2.imshow("Original",image)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Bulanik", image)
cv2.waitKey(0)
 
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)
cv2.waitKey(0)

cnts= cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count {} coins in this image".format(len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, 0, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)


cv2.drawContours(coins, cnts, 1, (0, 255, 0), 2)
cv2.drawContours(coins, cnts, 2, (0, 255, 0), 2)

for (i, c) in enumerate(cnts):
 (x, y, w, h) = cv2.boundingRect(c)

 print("Coin #{}".format(i + 1))
 coin = image[y:y + h, x:x + w]
 cv2.imshow("Coin", coin)
 mask = np.zeros(image.shape[:2], dtype = "uint8")
 ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
 cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
 mask = mask[y:y + h, x:x + w]
 cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask =mask))
 cv2.waitKey(0)