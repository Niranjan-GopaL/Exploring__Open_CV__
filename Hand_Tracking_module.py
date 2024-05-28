import cv2
import mediapipe as mp
# to check the FRAME RATE  
import time 

# Selecting WebCam if you have multiple webcams
# number :-  0 1 2 ... 
cap = cv2.VideoCapture(0) 



mpHands = mp.solutions.hands
hands = mpHands.Hands()

# mediaPipe provided us with functions that do the MATH
# there will be 21 points (landmarks or lms) and to connect each points  => HARD MATH !
mpDraw = mp.solutions.drawing_utils



# FRAME RATE CALCULATION ; ACCESSING EACH LANDMARK
prev_time = 0
curr_time = 0

# BASIC SNIPPET TO CALCULATE FPS
while 1:
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

while 1:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    many_hands = results.multi_hand_landmarks
    print(many_hands) 
    
    if many_hands :
        for  each_hand_lms in many_hands :
            # getting information of EACH HAND : id_no ; landmarks
            # todo :- what is (id,lm) pair - it seems we can access a landmark through ID but ALL THE INFORMATION IS STORED in lm
            for id, lm in enumerate(each_hand_lms.landmark) :
                # print(id,lm)  # this gives x,y,z co-ordniate in 
                # DECIMAL PLACES (ratio of co-ordinate's x value AND image windows' width)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                print(f'Landmark id : {id}, X :{cx}, Y : {cy}')

                # Accessing individual LANDMARK THROUGH id
                if id == 4:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                
            
            mpDraw.draw_landmarks(img, each_hand_lms , mpHands.HAND_CONNECTIONS)

    # Calculating the fps 
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
 
    # Render it in the IMAGE instead of CONSOLE 
    # print(f'FPS -----------> {round(fps,3)}')

    cv2.putText(img, str(round(fps,2)) , (10,70) , cv2.FONT_HERSHEY_SCRIPT_COMPLEX , 3 , (255,0,255) )
            
    cv2.imshow("Image",img)
    cv2.waitKey(1)