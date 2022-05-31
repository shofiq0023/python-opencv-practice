import cv2 as cv
import numpy as np

# blank = np.zeroes((500, 500, 3), dtype='uint8')
blank = np.zeros((500,500,3), dtype="uint8")
# img = imread("images/Cat.jpg")

# 1. Paint the image a certain color
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("Blank", blank)

# 2. Draw rectangle
# cv.rectangle(blank, (0,0), (250, 500), (0,0,255), thickness=cv.FILLED)
# cv.imshow("Rectangle", blank)

# 3. Draw circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (0,0,255), thickness=-1)
# cv.imshow("Circle", blank)

# 4. Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow("Circle", blank)

# 5. Write text
cv.putText(blank, "This is hello", (10,255), cv.FONT_HERSHEY_COMPLEX, 2.0, (0,0,255), thickness=5)
cv.imshow("text", blank)

cv.waitKey(0)

