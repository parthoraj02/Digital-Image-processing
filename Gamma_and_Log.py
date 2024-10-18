import cv2
import numpy as np

image = cv2.imread('bird.jpg', 0)

cv2.imshow('Original Image', image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

c = 1
gamma = 2.5

rows, cols = image.shape
gamma_transformed = np.zeros((rows, cols), dtype=np.float32)

for i in range(rows):
    for j in range(cols):
        gamma_transformed[i, j] = c * np.power(image[i, j], gamma)


cv2.imwrite('gamma_transformed_image.jpg', gamma_transformed)
im3 = cv2.imread('gamma_transformed_image.jpg')
cv2.imshow('Gamma Transformed Image', im3)
cv2.waitKey(4000)
cv2.destroyAllWindows()

rows, cols = gamma_transformed.shape
scaled_image = np.zeros((rows, cols), dtype=np.float32)

for i in range(rows):
    for j in range(cols):
        scaled_image[i, j] = c * np.power(image[i, j] / 255.0, gamma) * 255


cv2.imwrite('fixed_gamma.jpg', scaled_image)
im4 = cv2.imread('fixed_gamma.jpg', 0)
cv2.imshow('After Fixed (Gamma)', im4)
cv2.waitKey(2000)
cv2.destroyAllWindows()