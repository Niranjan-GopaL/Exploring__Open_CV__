import cv2
import mediapipe as mp
import time


# get vedios from pexels.com
cap = cv2.VideoCapture('PoseVideos/3.mp4')

window_tile = "After Resizing"

curr_time = prev_time = 0

def resize_saviour(capture) :
    ret, frame = capture.read()
    if not ret : return [ 0 ]

    # Get the current frame size
    height, width, _ = frame.shape

    # Resize the frame
    scale_percent = 20
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    dim = (new_width, new_height)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    return resized



# Basic frame_work
while 0:
    success, img = cap.read()

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time


    window_name = "Video is just many images"
    # STARTED READING DOCUMENTATION OF open_cv and IT'S INSANE
    # cv2.imshow(window_name, img)
    # cv2.moveWindow(window_name, 100, 100)   # Move you're top left corner's co-ordinate (just like electronjs)
    # cv2.resizeWindow(window_name, 500, 500) # resizes the window ; But video is not Scaled appropriatly 

    cv2.putText(img, str(round(fps,2)) , (10,70) , cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,255) )
    return_ = resize_saviour(cap)
    
    if return_ : break

    # 10ms delay
    cv2.waitKey(1)



mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

while 1:
    success, img = cap.read()

    # print(results.pose_landmarks)

    resize_fn_return_img = resize_saviour(cap)
    if not resize_fn_return_img.any() : break
    
    imgRGB = cv2.cvtColor(resize_fn_return_img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    
    if results.pose_landmarks:
        # mpDraw.draw_landmarks(img, results.pose_landmarks )
        mpDraw.draw_landmarks(resize_fn_return_img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, _ = resize_fn_return_img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(resize_fn_return_img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    # fps calc
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time


    cv2.putText(resize_fn_return_img, str(round(fps,2)) , (0,0) , cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,255) )

    # Display the resized frame
    cv2.imshow(window_tile , resize_fn_return_img )

    # 10ms delay
    k = cv2.waitKey(10) & 0xff
    if k == 27: break
