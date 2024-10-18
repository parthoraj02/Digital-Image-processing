import cv2


img = cv2.imread('bird.jpg', 1)


# Print original image properties (uncomment if needed)
print(img.shape)
#print(img.size)

# print(" Image as 2D Array:\n", img)

# print("Image " ,img[50, 50])
# cv2.imshow('Color  image', img[100:300,300:700])
# cv2.waitKey(3000)
print(img[100:300,300:700])
# img3=255-img
# cv2.imshow('Color Negative image', img3)
# cv2.waitKey(3000)
# cv2.imshow('Grey image', im2)
# cv2.waitKey(3000)
# im4=255-im2
# cv2.imshow('Grey Negative image', im4)
# cv2.waitKey(3000)

img[100:300,300:700] =171

#print(img[50:60, 50:60],"\n" ,img[70:80, 50:60])
cv2.imshow('Negative image', img)
cv2.waitKey(3000)


# Print the modified array
print("Modified Image as 2D Array:\n", img)

# Save the modified image
# cv2.imwrite('modified_reverse.jpeg', img)

# Show the modified image
# cv2.imshow('Modified image', img)
# cv2.waitKey(5000)
cv2.destroyAllWindows()

import cv2
import math


def log_transform_manual(img, c):
    # Get image dimensions
    height, width = img.shape

    # Initialize an empty list (or array) for the transformed image
    log_t = [[0] * width for _ in range(height)]

    # Apply the log transformation manually using loops
    for i in range(height):
        for j in range(width):
            # Apply the log transformation to each pixel
            log_t[i][j] = c * math.log(1 + img[i][j])

    return log_t


# Load an image (grayscale)
img = cv2.imread('bird.jpg', 0)

if img is None:
    raise ValueError("Image not found or could not be loaded")

c = 2  # Scaling factor

# Apply the manual log transformation
log_t_manual = log_transform_manual(img, c)

# Print the log-transformed image (as a list of lists)
print("Log Transformed Image (Manual):")
for row in log_t_manual:
    print(row)

