import cv2
import mediapipe as mp
# to check the FRAME RATE  
import time 

# Selecting WebCam if you have multiple webcams
# number :-  0 1 2 ... 
cap = cv2.VideoCapture(0) 

 
#  todo :- We'll Implement this ourselves later
mpHands = mp.solutions.hands
hands = mpHands.Hands()
 
 
 
# Fundamental Code to run our Webcam
while 1:
    success, img = cap.read()

    cv2.imshow("Image",img)

    cv2.waitKey(1)




