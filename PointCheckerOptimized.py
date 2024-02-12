import numpy as np
from PIL import ImageGrab
import pyautogui

#min_colors = np.array([(15, 230, 190), (15, 215, 110), (150, 100, 220)])
#max_colors = np.array([(50, 250, 255), (30, 245, 130), (210, 130, 255)])

min_colors = np.array([(0, 150, 100), (0, 150, 100), (150, 50, 150)])
max_colors = np.array([(100, 250, 255), (80, 245, 150), (210, 130, 255)])

keys = ['up', 'left', 'f']
key_states = {key: False for key in keys}


def checker(x1, y1, x2, y2):
    #img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    img = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    pixels = np.array(img)
    #pixels = np.array([img.getpixel((x, y)) for x, y in points])
    for i in range(len(keys)):
        mask = np.all((min_colors[i] <= pixels) & (pixels <= max_colors[i]), axis=2)
        if np.any(mask):
            if not key_states[keys[i]]:
                pyautogui.keyDown(keys[i])
                key_states[keys[i]] = True
        else:
            if key_states[keys[i]]:
                pyautogui.keyUp(keys[i])
                key_states[keys[i]] = False
