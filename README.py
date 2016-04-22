# tallervertical2016
import cv2
import imutils

image=cv2.imread("/home/manuel/tallervertical2016/scripts/pics/1.jpg")
resized=imutils.resize(image,200)
(h,w)= resized.shape[:2]
gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
ruta=gray[0:h/2-35,(w/2):w]
#ruta=cv2.equalizeHist(rutaq)

#ruta2=cv2.adaptiveThreshold(ruta,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,21,35)
ret,ruta2=cv2.threshold(ruta,127,255,cv2.THRESH_BINARY_INV)
#ruta2=cv2.adaptiveThreshold(ruta,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,19)

rutaq=imutils.resize(ruta2,200)
rutar=cv2.equalizeHist(rutaq)
rutarx=imutils.resize(ruta2,200)

#cv2.imwrite("mod.jpg",rutarx)
contours,_=cv2.findContours(rutarx,1,2)[-2:]
i=1000
j=0
k=0
for contour in contours:
	x,y,w,h=cv2.boundingRect(contour)
	if (h>60 or h<20) and (w>120 or w<60):
		continue	
#	cv2.rectangle(rutar,(x,y),(x+w,y+h),(255,255,255),2)	
#	cv2.imwrite("mod.jpg",rutarx)
	if x<i:
		i=x
		j=y	
		if h>40:
			k=h
		else:
			k=50
final=rutar[j-15:j+k,i:i+180]
finalr=imutils.resize(final,250)
blur=cv2.medianBlur(finalr,5)
#cv2.imshow("final",blur)
#cv2.imshow("original",resized)
#cv2.imshow("noeq",rutaq)
#cv2.imshow("eq",rutar)
cv2.imwrite("/home/manuel/tallervertical2016/scripts/readme.jpg",blur)
#cv2.waitKey(0)
