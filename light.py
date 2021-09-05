import cv2
video_capture=cv2.VideoCapture(0+cv2.CAP_DSHOW)
def nolight():
	return video_capture.read()