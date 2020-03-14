import subprocess
def install(name):
	subprocess.call(['pip','install',name])
install('matplotlib')
install ('opencv-python')
import numpy as np
import cv2
import matplotlib.pyplot as plt
"""
#A.vido capture and mask apply demo

cap=cv2.VideoCapture(0)
while(cap.isOpened()):
	c,fr=cap.read()
	hsv=cv2.cvtColor(fr,cv2.COLOR_BGR2HSV)
	lb=np.array([110,50,50])
	ub=np.array([130,255,255])
	mask=cv2.inRange(hsv,lb,ub)
	res=cv2.bitwise_and(fr,fr,mask=mask)
	cv2.imshow('hsv',hsv)
	cv2.imshow('orgframe',fr)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	if cv2.waitKey(1)& 0xFF==ord('q'):
		break
cap.release()
"""

"""
#B.green to hsv demo here we take a green color and we apply some hsv values on it
green=np.uint8([[[64, 128, 76]]])
green2hsv=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(green.shape)
print(green2hsv.shape)
resized_green=cv2.resize(green,(1000,710),cv2.INTER_AREA)
resized_hsv=cv2.resize(green2hsv,(1000,710),cv2.INTER_AREA)
cv2.imshow('hsv',resized_hsv)
cv2.imshow('g',resized_green)
print(resized_green.shape)
print(resized_hsv.shape)
cv2.waitKey(0)
"""
"""
#C.Thresholding
img1=cv2.imread('1.jpg',0)
img=cv2.medianBlur(img1,5)
ret,th1=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (value = 100)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
imgs=[img,th1,th2,th3]
for i in range(len(imgs)):
	plt.subplot(2,2,i+1),plt.imshow(imgs[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()
"""

"""
#D.edge detection
cap=cv2.VideoCapture(0,0)
while(cap.isOpened()):
	c,f=cap.read(0)
	f=cv2.flip(f,1)
	gray=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
	edg=cv2.Canny(f,100,100)
	cv2.imshow('gray',gray)
	cv2.imshow('color',f)
	cv2.imshow('edg',edg)
	if cv2.waitKey(1)&0xFF==ord('q'):
		break
cap.release()
"""
"""
#E.ploting 
f=cv2.imread('1.jpg')
plt.subplot(121),plt.title('ldksja'),plt.xticks([101]),plt.yticks([110])
plt.show()
"""
"""
#F.video capture
cap=cv2.VideoCapture(0)
frcc=cv2.VideoWriter_fourcc(*'mp4v')
op=cv2.VideoWriter('m.mp4',frcc,20.0,(640,480))
while (cap.isOpened()):
	c,f=cap.read()
	if c==True:
		f=cv2.flip(f,1)
		op.write(f)
		cv2.imshow('video',f)
		if cv2.waitKey(1)&0xFF==ord('q'):
			break
	else:
		break
cap.release()
op.release()
"""		
"""
#G.lines detection
img=cv2.imread('2.jpg')
img=cv2.resize(img,(1000,720),cv2.INTER_AREA)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edg=cv2.Canny(gray,50,150,3)
cv2.imshow('edg',edg)
cv2.imshow('colorimg',img)
cv2.waitKey(0)
"""
"""
#H.face extraction
f=cv2.imread('2.jpg')
fcd=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
fcs=fcd.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in fcs:
#		cv2.rectangle(f,(x,y),(x+w,y+h),(255,255,0),3) #you adjust parameters
		cv2.imwrite('kkk.jpg',f[x:y,x+w:y+h])

f=cv2.resize(f,(720,640),cv2.INTER_AREA)
cv2.imshow('img',f)
		
cv2.waitKey(0)
"""

"""
#I.capture video face and eye

import cv2
fcd=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ecd=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
	c,f=cap.read()
	f=cv2.flip(f,1)
	gray=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
	fc=fcd.detectMultiScale(gray,1.1,4)
	for(x,y,w,h) in fc:
		cv2.rectangle(f,(x,y),(x+w,y+h),(255,255,0),2)
		roigr=gray[y:y+h,x:x+w]
		roicr=f[y:y+h,x:x+w]
		eye=ecd.detectMultiScale(roigr)
		for (ex,ey,eh,ew) in eye:
			cv2.rectangle(roicr,(ex,ey),(ex+ew,ey+eh),(255,255,2))
		
	cv2.imshow("cl",f)	
	if cv2.waitKey(1)&0xFF==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
"""

"""
#print(cv2.getPerspectiveTransform)
#cv2.waitKey(0)	#waits for the given time if it is zero wait untill we close 
"""
cv2.destroyAllWindows()
