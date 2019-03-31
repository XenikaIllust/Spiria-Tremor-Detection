import cv2
import numpy as np

im = cv2.imread("../new_dataset/HealthySpiral/sp1-H1.jpg")
# im[:,:,1] = 255
# im[:,:,2] = 255

# Increase saturation

# Merging saturated matrices

full_1 = 255 * np.ones(im.shape)

im_clone = im.copy()

a = np.where(im_clone > np.array([150, 150, 150]))
im_clone[a] = 255
cv2.imshow("test", im_clone)
cv2.waitKey()

blur = cv2.GaussianBlur(im_clone[:,:,0],(5,5),0)
cv2.imshow("test", blur)
cv2.waitKey()

ret3,th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
res = th3 - im_clone[:,:,0]
cv2.imshow("test", res)
cv2.waitKey()


cv2.imshow("test", th3)
cv2.waitKey()