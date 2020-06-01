import numpy as np
from PIL import ImageGrab
import cv2
 
while(True):
	OrnekResim 							=	cv2.imread('Kaktus.jpg') #Tespit Edeceğimiz Resim
	OrnekResimDonustur 					=	cv2.cvtColor(OrnekResim,cv2.COLOR_BGR2GRAY) #Tespit Edeceğimiz Resimi Gri Formata Donustur
	EkranGoruntusu 						=	np.array(ImageGrab.grab(bbox=(0,40,850,640))) #Anlik Ekran Goruntusunu Al
	EkranGoruntusuDonustur 				=	cv2.cvtColor(EkranGoruntusu,cv2.COLOR_BGR2GRAY) #Ekran Goruntusunu Gri Formata Donusturuyoruz
	Sonuc 								=	cv2.matchTemplate(EkranGoruntusuDonustur,OrnekResimDonustur,cv2.TM_CCOEFF_NORMED) #Ekran Grountusunun Icerisinde Resmi Ariyoruz
	sin_val, max_val, min_loc, max_loc	=	cv2.minMaxLoc(Sonuc) #Bulunan Objenin Koordinatlarini Bul
	Ust_Sol 							=	max_loc #Bulunan Objenin Ust ve Sol Uzakligi
	Alt_Sag								=	(Ust_Sol[0]+50, Ust_Sol[1]+50) #Bulunan Objenin Alt ve Sag Uzakligi
	cv2.rectangle(EkranGoruntusu, Ust_Sol, Alt_Sag, (0,255,0),5) #Ekranda Bulunan Nesnenin Koordinatlarini Isaretle
	cv2.imshow('EKRAN',EkranGoruntusu) #Ekran Goruntusunu Goster
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break