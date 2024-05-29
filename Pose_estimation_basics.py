import cv2
import mediapipe as mp
import time


# get vedios from pexels.com
cap = cv2.VideoCapture('PoseVideos/3.mp4')

window_tile = "After Resizing"

curr_time = prev_time = 0

# given a VideoCapture Object, this fn returns' it's resizes `img: MatLike`
def resize_saviour(capture) :
    ret, frame = capture.read()
    if not ret : return (False, [0])

    # Get the current frame size
    height, width, _ = frame.shape

    # Resize the frame
    scale_percent = 20
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    dim = (new_width, new_height)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    return (True, resized)



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
    # success, img = cap.read() # first we need to resize this image 
    success, resized_img = resize_saviour(cap)
    if not success : break

    # todo :- what does this do ? media_pipe wants image to be in RGB for it to detect the poses
    imgRGB = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB) 
    # print(results.pose_landmarks)
    
    if results.pose_landmarks:
        # # We can see just the dots
        # mpDraw.draw_landmarks(img, results.pose_landmarks )                                       

        # We can see connections also 
        mpDraw.draw_landmarks(resized_img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)         

        # https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker   <-- markings for all landmarks : feature on body
        # 0: nose  ; 1: left_eye_inner ; 2: left_eye
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, _ = resized_img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            if id == 20 :
                # id number 20 will be in blue dot
                cv2.circle(resized_img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    # fps calc
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(resized_img, str(round(fps,2)) , (0,0) , cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,255) )

    # Display the resized frame
    cv2.imshow(window_tile , resized_img )

    # 10ms delay
    k = cv2.waitKey(10) & 0xff
    if k == 27: break
