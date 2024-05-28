import cv2
import mediapipe as mp
# to check the FRAME RATE  
import time 

# Selecting WebCam if you have multiple webcams
# number :-  0 1 2 ... 
cap = cv2.VideoCapture(0) 

'''
There are only 3 sections in this code :-
- Most fundamental code to get you're camera feed
- to see landmarks in our Hand ; connect landmarks
- to display fps 

Folds are such awesome tool
Create a fold :- ctrl + k ctrl + ,
Remove a fold :- ctrl + k ctrl + .
'''


# Fundamental Code to run our Webcam
while 0:
    success, img = cap.read()

    cv2.imshow("Image",img)

    cv2.waitKey(1)

 
 # Displya the Hand Landmarks and 
 
#  todo :- We'll Implement this ourselves later
mpHands = mp.solutions.hands
hands = mpHands.Hands()

# mediaPipe provided us with functions that do the MATH
# there will be 21 points (landmarks or lms) and to connect each points  => HARD MATH !
mpDraw = mp.solutions.drawing_utils

while 0:
    success, img = cap.read()

    # todo :- what does this do ?
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    # to check if there is a hand or not ; 
    # IF THERE IS A HAND => printing out the co-ordinates of hands 
    # otherwise value is None
    many_hands = results.multi_hand_landmarks
    print(many_hands) 
    
    if many_hands :
        for  each_hand_lms in many_hands :
            # mpDraw.draw_landmarks(img, each_hand_lms )  # draws the dots ONLY, below joins the connections also
            mpDraw.draw_landmarks(img, each_hand_lms , mpHands.HAND_CONNECTIONS)
    
    # cv2.imshow("Image",imgRGB)
    cv2.imshow("Image",img)
    cv2.waitKey(1)



# FRAME RATE CALCULATION and Displaying it
prev_time = 0
curr_time = 0

# BASIC SNIPPET TO CALCULATE FPS
''' 
curr_time = time.time()
fps = 1 / (curr_time - prev_time)
prev_time = curr_time
'''

while 1:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    many_hands = results.multi_hand_landmarks
    print(many_hands) 
    
    if many_hands :
        for  each_hand_lms in many_hands :
            mpDraw.draw_landmarks(img, each_hand_lms , mpHands.HAND_CONNECTIONS)

    # Calculating the fps 
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    print(f'FPS -----------> {round(fps,3)}')
 
    # Render it in the IMAGE instead of CONSOLE 
    # cv2.putText(img, )
            
    cv2.imshow("Image",img)
    cv2.waitKey(1)