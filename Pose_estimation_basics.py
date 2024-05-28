import cv2
import mediapipe as mp
import time


# get vedios from pexels.com
cap = cv2.VideoCapture('PoseVideos/3.mp4')

curr_time = 0
prev_time = 0

def resize(capture, window_tile="Resized Video") :
    ret, frame = capture.read()
    if not ret : return 1

    # Get the current frame size
    height, width, _ = frame.shape

    # Resize the frame
    scale_percent = 25
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    dim = (new_width, new_height)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    # Display the resized frame
    cv2.imshow(window_tile , resized)

    # Wait for a key press
    k = cv2.waitKey(30) & 0xff
    if k == 27: return 1



while 1:
    success, img = cap.read()

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(img, str(round(fps,2)) , (10,70) , cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,255) )
 

    window_name = "Video is just many images"
    # cv2.imshow(window_name, img)
    # cv2.moveWindow(window_name, 100, 100)
    # cv2.resizeWindow(window_name, 500, 500) # resizes the window ; But video is not Scaled appropriatelt

    return_ = resize(cap)
    if return_ : break
    
    # 10ms delay
    cv2.waitKey(1)
