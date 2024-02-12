from PIL import ImageGrab
import pyautogui

# min_blue = (0, 190, 235)
# max_blue = (50, 255, 250)
# min_green = (0, 220, 120)
# max_green = (5, 255, 130)
# min_violet = (170, 100, 240)
# max_violet = (230, 125, 255)


def checker(points):
    img = ImageGrab.grab()
    for x, y in points:
        color = img.getpixel((x, y))
        if (0 <= color[0] <= 50) and (190 <= color[1] <= 255) \
                and (235 <= color[2] <= 250):
            pyautogui.keyDown('up')
        else:
            pyautogui.keyUp('up')
        if (0 <= color[0] <= 5) and (220 <= color[1] <= 255) \
                and (120 <= color[2] <= 130):
            pyautogui.keyDown('left')
        else:
            pyautogui.keyUp('left')
        if (170 <= color[0] <= 230) and (100 <= color[1] <= 125) \
                and (240 <= color[2] <= 255):
            pyautogui.keyDown('f')
        else:
            pyautogui.keyUp('f')
