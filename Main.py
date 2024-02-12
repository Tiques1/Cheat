import keyboard
from pynput.mouse import Listener
import threading
import time
import PointChecker

flag = True


def start_listener():
    a, b = None, None
    global flag
    flag = False

    def on_click(x, y, button, pressed):
        nonlocal a, b
        if pressed:
            a = [x, y]
        else:
            b = [x, y]
            listener.stop()

    with Listener(on_click=on_click) as listener:
        listener.join()

    flag = True
    threading.Thread(target=thread_generator, args=bresenham_line(a[0], a[1], b[0], b[1])).start()


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


def thread_generator(points):
    while flag:
        threading.Thread(target=PointChecker.checker, args=points).start()
        time.sleep(10)


keyboard.add_hotkey('ctrl+alt+q', start_listener)
keyboard.wait('esc')
