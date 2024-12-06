import cv2
import pyautogui
import numpy

wwidth = 450
wheight = 450
cursorpos = pyautogui.position()

nposx = cursorpos.x - 225
nposy = cursorpos.y - 225

while True == True:
    im = numpy.array(pyautogui.screenshot(region=((nposx, nposy) + (wwidth, wheight))))

    cursorpos = pyautogui.position()
    nposx = cursorpos.x - wwidth/2
    nposy = cursorpos.y - wheight/2

    cv2.imshow("Press Q to kill window", im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
