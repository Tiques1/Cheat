import numpy as np
import pyautogui

min_colors = np.array([(15, 220, 190), (15, 215, 110), (150, 100, 220)])
max_colors = np.array([(170, 255, 255), (150, 245, 180), (210, 130, 255)])

keys = ['up', 'left', 'f']
key_states = {key: False for key in keys}


def checker(x1, y1, x2, y2):
    img = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    pixels = np.array(img)
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
