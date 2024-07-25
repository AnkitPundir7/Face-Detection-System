import cv2
#dataset load
trainedData=cv2.CascadeClassifier('Face.xml')
#choose a image
img=cv2.imread('six.jpg')

#Conversion to greyscale bcz open cv works only on greyscale
greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



#detect faces
faceCoordinates=trainedData.detectMultiScale(greyimg)
print(faceCoordinates)

# print(faceCoordinates)
# [[367 120 246 246]]

for x,y,w,h in faceCoordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


#resizing the image
img=cv2.resize(img,(700,700))

#display image
cv2.imshow('Multi person',img)


#pause execution of the program until a key is pressed
cv2.waitKey()

print('End of program')
