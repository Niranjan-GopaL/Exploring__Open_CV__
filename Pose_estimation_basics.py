import cv2
import mediapipe as mp
import time


mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


# get vedios from pexels.com
cap = cv2.VideoCapture('PoseVideos/3.mp4')


