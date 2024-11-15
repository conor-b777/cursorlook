import cv2
import pyautogui
import numpy

cursorpos = pyautogui.position()
halfx = cursorpos.x%2
halfy = cursorpos.y%2

nposx = cursorpos.x - halfx
nposy = cursorpos.y - halfy

while True == True:
    im = numpy.array(pyautogui.screenshot(region=((nposx, nposy) + (450, 450))))

    cursorpos = pyautogui.position()
    halfx = cursorpos.x%2
    halfy = cursorpos.y%2

    nposx = cursorpos.x - halfx
    nposy = cursorpos.y - halfy

    cv2.imshow("Press Q to kill window", im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
