import cv2
import numpy as np

def log_fun(img,c):
    hight,width=img.shape
    logg_t=np.zeros((hight,width),dtype=np.float32)

    img_float = img.astype(np.float32)
    for i in range(hight):
         for j in range(width):
             logg_t[i,j]=c*np.log(img_float[i,j]+1)



    #log_t = c * np.log(1 + img_float)
    cv2.imwrite('newt.jpg',logg_t)
    #
    print("before")
    print(logg_t)
    log_p=cv2.imread('newt.jpg',0)
    print("after")
    print(log_p)
    cv2.imshow("log transformed ",log_p)
    cv2.waitKey(5000)
    log_float = log_p.astype(np.float32)
    log_con=255*(log_float-log_float.min())/(log_float.max()-log_float.min())
    log_con=log_con.astype("uint8")
    cv2.imshow("log conformed ", log_con)
    cv2.waitKey(5000)
def gamma_fun(img,c,gm):
    img_g=c*(img**gm)
    cv2.imwrite('newG.jpg',img_g)
    #print(log_t)
    gamma_q=cv2.imread('newG.jpg',0)
    print(gamma_q)
    cv2.imshow("Gamma transformed ",img_g)
    cv2.waitKey(5000)
    img_g = gamma_q.astype(np.float32)
    gamma_con=255*(img_g-img_g.min())/(img_g.max()-img_g.min())
    gamma_con=gamma_con.astype("uint8")
    print(gamma_con)
    cv2.imshow("gamma conformed ", gamma_con)
    cv2.waitKey(5000)

# Load an image
img = cv2.imread('bird.jpg', 0)
# Display the original image
cv2.imshow('Original Image', img)

# Wait for 1000 milliseconds (1 second)
cv2.waitKey(1000)

if img is None:
    raise ValueError("Image not found or could not be loaded")
log_fun(img,2)
#gamma_fun(img,1,1)


cv2.destroyAllWindows()

