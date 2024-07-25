import cv2
#dataset load
trainedData=cv2.CascadeClassifier('Face.xml')
#start the webcam
cam=cv2.VideoCapture('ayush.mp4')
while True:
    success,frame=cam.read()

    #Conversion to greyscale bcz open cv works only on greyscale
    greyimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #detect faces
    faceCoordinates=trainedData.detectMultiScale(greyimg)


    for x,y,w,h in faceCoordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    #resizing the image
    frame=cv2.resize(frame,(700,600))

    #display image
    cv2.imshow('video',frame)


    #pause execution of the program until a key is pressed
    key=cv2.waitKey(1)
    if(key==81 or key==113):
        break
cam.release()
print('End of program')
'''
#resizing the image
img=cv2.resize(img,(700,700))




'''
