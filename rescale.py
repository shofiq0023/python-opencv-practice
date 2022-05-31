import cv2 as cv

################### Resizing images and video ###################
img = cv.imread("images/boy.jpeg")

# cv.imshow("Boy", img)

def rescaleFrame(frame, scale=0.75):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img, scale=.2)
cv.imshow("Boy", resized_image)

cv.waitKey(0)