import cv2
import pyautogui
import numpy

cursorpos = pyautogui.position()

while True == True:
    im = numpy.array(pyautogui.screenshot(region=((cursorpos) + (300, 300))))

    cursorpos = pyautogui.position()

    cv2.imshow("cursor", im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
