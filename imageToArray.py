import cv2
import numpy as np

# Load the color image
img = cv2.imread('bird.jpg', 0)

c = 50
img = img.astype(np.float64)
log_transformed = c * np.log(1 + img)
cv2.imshow('before',log_transformed)
cv2.waitKey(1000)
print(log_transformed)
print(log_transformed.max())
print(log_transformed.min())
q=255*(log_transformed-log_transformed.min())/(log_transformed.max()-log_transformed.min())
q = np.uint8(q)
cv2.imshow('after',q)
cv2.waitKey(1000)
print(q)
abc=cv2.imwrite('log.jpg',log_transformed)
img2=cv2.imread('log.jpg',0)
print("next")
print(img2)

cv2.imshow('save before convert image',img2)
cv2.waitKey(2000)
#log_transformed = np.array(log_transformed, dtype=np.uint8)
p = 255 * (img2 - img2.min()) / (img2.max() - img2.min())

#print(img2.max())
#cv2.imshow('Grayscale Image23', q)
cv2.waitKey(2000)
#cv2.imshow('Grayscale Image', p)


#cv2.imshow('Log Transformed Image', log_transformed)

cv2.waitKey(3000)
cv2.destroyAllWindows()

    # Optionally save the log-transformed image
cv2.imwrite('log_transformed_bird.jpg', log_transformed)