import cv2
import numpy as np

img = cv2.imread('bird.jpg', 1)

# cv2.imshow('Color  image', img)
# cv2.waitKey(2000)
# b, g, r = cv2.split(img)
# greyImage=r*.3+g*.6+b*.1
# print(greyImage)
# greyImage = greyImage.astype(np.uint8)
#
#
# cv2.imshow('grey  image', greyImage)


# Show the Blue, Green, and Red channels
# cv2.imshow('Blue Channel', b)
# cv2.imshow('Green Channel', g)
# cv2.imshow('Red Channel', r)


cv2.waitKey(3000)

cv2.destroyAllWindows()
