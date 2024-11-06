import cv2

image = cv2.imread("blue.png")

while True == True:
    cv2.imshow("Say it Ain't So", image,)
    if cv2.waitKey(1) & 0xFF == ord('q'): break