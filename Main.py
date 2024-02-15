import keyboard
from pynput.mouse import Listener
import threading
import ColorChecker as pc


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
    threading.Thread(target=thread_generator, args=[min(a[0], b[0]), min(a[1], b[1]),
                                                            max(a[0], b[0]), max(a[1], b[1])]).start()


def thread_generator(x1, y1, x2, y2):
    while flag:
        t = threading.Thread(target=pc.checker, args=(x1, y1, x2, y2))
        t.start()
        t.join()


keyboard.add_hotkey('ctrl+alt+q', start_listener)
keyboard.wait('esc')
