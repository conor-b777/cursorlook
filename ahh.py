import cv2
import pyautogui
import numpy

cursorpos = pyautogui.position()

while True == True:
    im = numpy.array(pyautogui.screenshot(region=((cursorpos) + (250, 250))))

    cursorpos = pyautogui.position()

    cv2.imshow("where ur cursor is", im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
