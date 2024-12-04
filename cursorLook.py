import cv2
import pyautogui
import numpy

cursorpos = pyautogui.position()

nposx = cursorpos.x - 225
nposy = cursorpos.y - 225

while True == True:
    im = numpy.array(pyautogui.screenshot(region=((nposx, nposy) + (450, 450))))

    cursorpos = pyautogui.position()
    nposx = cursorpos.x - 225
    nposy = cursorpos.y - 225

    cv2.imshow("Press Q to kill window", im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
