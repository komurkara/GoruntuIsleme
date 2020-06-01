import numpy as np # Bulantı filtre fonksiyonunu uygulamaak için kütüphane      
import cv2 #Görüntüyü açmak için opencv kütüphanesi

gezegenler = cv2.imread("p.jpg") #Resmi okuma
gray = cv2.cvtColor(gezegenler, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow("Blurr", blurred)
cv2.waitKey(0)

kenar = cv2.Canny(blurred, 30, 150)
#Canny ile edge detection yaptık 2 tane threshold değeri var.10 dan küçük için kenar yok, 60 dan büyük için kenar vardır.
cv2.imshow("Canny", kenar) #Resmi gösterme
cv2.waitKey(0)

cnts = cv2.findContours(kenar.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Bulunan gezegen sayısı = {}".format(len(cnts)))

sayaclar = gezegenler.copy()
cv2.drawContours(sayaclar, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Sayac",sayaclar)

cv2.waitKey(0)

for(i,j) in enumerate(cnts):
    (x,y,z,h) = cv2.boundingRect(j)
    
    print("gezegenler : {}".format(i+1))
    sayac = gezegenler[y:y+h, x:x+v]
    cv2.imshow("Sayac",sayac)
    
    maske = np.zeros(gezegenler.shape[:2], dtype=np.uint8)
    ((centerX, centerY),radius) = cv2.minEnclosingCircle(j)
    cv2.circle(maske, (int(centerX), int(centerY)), int(radius), 255, -1)
    maske = maske[y:y+h, x:x+v]
    cv2.imshow("gezegende maske ", cv2.bitwise_and(sayac, sayac, mask = maske))
    cv2.waitKey(0)