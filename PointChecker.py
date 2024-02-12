from PIL import ImageGrab
import pyautogui

min_blue = (0, 190, 235)
max_blue = (50, 255, 250)
min_green = (0, 220, 120)
max_green = (5, 255, 130)
min_violet = (170, 100, 240)
max_violet = (230, 125, 255)


def checker(a, b):
    points = bresenham_line(a[0], a[1], b[0], b[1])
    while True:
        img = ImageGrab.grab()
        for x, y in points:
            color = img.getpixel((x, y))
            if is_color_in_range(color, min_blue, max_blue):
                pyautogui.keyDown('up')
            else:
                pyautogui.keyUp('up')
            if is_color_in_range(color, min_green, max_green):
                pyautogui.keyDown('left')
            else:
                pyautogui.keyUp('left')
            if is_color_in_range(color, min_violet, max_violet):
                pyautogui.keyDown('f')
            else:
                pyautogui.keyUp('f')


def is_color_in_range(pixel_color, min_color, max_color):
    r, g, b = pixel_color
    min_r, min_g, min_b = min_color
    max_r, max_g, max_b = max_color

    return (min_r <= r <= max_r) and (min_g <= g <= max_g) and (min_b <= b <= max_b)


def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while x0 != x1 or y0 != y1:
        points.append((x0, y0))
        err2 = 2 * err
        if err2 > -dy:
            err -= dy
            x0 += sx
        if err2 < dx:
            err += dx
            y0 += sy
    points.append((x0, y0))
    return points
