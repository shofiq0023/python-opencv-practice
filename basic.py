import cv2 as cv

img = cv.imread("images/park.jpg")
cv.imshow("Cat", img)

# Convert to greyscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", grey)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge detection
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny edge", canny)

cv.waitKey(0)