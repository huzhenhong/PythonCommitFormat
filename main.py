import cv2

img = cv2.imread("circle.png")

img = cv2.resize(img, (256, 256))

replicate = cv2.copyMakeBorder(img, 20, -20, 20, 20, cv2.BORDER_REPLICATE)
