import cv2
import pyautogui
import numpy

cursorpos = pyautogui.position()
halfx = cursorpos.x%2
halfy = cursorpos.y%2

nposx = cursorpos.x - halfx
nposy = cursorpos.y - halfy

print(f"{cursorpos}")

while True == True:
    im = numpy.array(pyautogui.screenshot(region=((nposx, nposy) + (300, 300))))

    cursorpos = pyautogui.position()
    halfx = cursorpos.x%2
    halfy = cursorpos.y%2

    nposx = cursorpos.x - halfx
    nposy = cursorpos.y - halfy

    cv2.imshow("cursor", im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
