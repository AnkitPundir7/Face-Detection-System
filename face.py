import cv2
#dataset load
trainedData=cv2.CascadeClassifier('Face.xml')
#choose a image
img=cv2.imread('my.jpg')

#Conversion to greyscale bcz open cv works only on greyscale
greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect faces
faceCoordinates=trainedData.detectMultiScale(greyimg)

print(faceCoordinates)
# [[367 120 246 246]]

x,y,w,h=faceCoordinates[0]
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,254),5)

#resizing the image
img=cv2.resize(img,(700,700))

#display image
cv2.imshow('Single person',img)

#pause execution of the program until a key is pressed
cv2.waitKey()

print('End of program')
