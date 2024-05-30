import cv2
import mediapipe as mp
import time 



# given a VideoCapture Object, this fn returns' it's resizes `img: MatLike`
def resize_saviour(capture,scale_percent = 60) :
    ret, frame = capture.read()
    if not ret : return (False, [0])

    # Get the current frame size
    height, width, _ = frame.shape

    # Resize the frame
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    dim = (new_width, new_height)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    return (True, resized)



''' File names
Face_1_2160_3840_25fps.mp4 
Face_2_2160_4096_25fps.mp4
Face_3_4096_2160_25fps.mp4
Face_4_3840_2160_25fps.mp4
'''
cap = cv2.VideoCapture("Videos/Face_4_3840_2160_25fps.mp4")

# Basic Code
while 0 : 
    success, resized_img = resize_saviour(cap,30)
    if not success : break
    cv2.imshow("Image shown", resized_img)
    cv2.waitKey(5)

pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)

while True:
    success, img = resize_saviour(cap,20)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            # mpDraw.draw_detection(img, detection)
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih),
            int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(img, f'{int(detection.score[0] * 100)}%',
           (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
            2, (255, 0, 255), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
    3, (0, 255, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
