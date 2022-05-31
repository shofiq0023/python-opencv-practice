import cv2 as cv

################### Reading image ###################
# img = cv.imread("images/Cat.jpg")

# cv.imshow("Cat", img)

# cv.waitKey(0)

################### Reading Video files ###################
capture = cv.VideoCapture('videos/dog.mp4');

# To capture with web cam. 0, 1, 2, 3 indicates the camera connected to your device
# capture = cv.VideoCapture(0)

while True:
	isTrue, frame = capture.read()
	cv.imshow("video", frame)

	if cv.waitKey(20) & 0xFF==ord("s"):
		break

capture.release()
cv.destroyAllWindows()



