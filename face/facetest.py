import subprocess
def install(name):
	subprocess.call(['pip','install',name])
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
