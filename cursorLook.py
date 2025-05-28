import cv2
import pyautogui
import numpy

wwidth = 475
wheight = 475
cursorpos = pyautogui.position()

nposx = cursorpos.x - wwidth/2
nposy = cursorpos.y - wheight/2

while True:
    im = numpy.array(pyautogui.screenshot(region=((nposx, nposy) + (wwidth, wheight))))
    colorImg = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    cursorpos = pyautogui.position()
    nposx = cursorpos.x - wwidth/2
    nposy = cursorpos.y - wheight/2

    if not nposx < 5 or not nposy < 5:
        cv2.imshow("Press Q to kill window", colorImg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
