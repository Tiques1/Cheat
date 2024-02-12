import keyboard
from pynput.mouse import Listener
import draw_line as dl
import threading


def start_listener():
    a, b = None, None

    def on_click(x, y, button, pressed):
        nonlocal a, b
        if pressed:
            a = [x, y]
            # print(f'Нажата кнопка {button} в точке: x={x}, y={y}')
        else:
            # print(f'Отпущена кнопка {button} в точке: x={x}, y={y}')
            b = [x, y]
            listener.stop()

    with Listener(on_click=on_click) as listener:
        listener.join()

    threading.Thread(target=dl.line, args=(a, b)).start()


keyboard.add_hotkey('ctrl+alt+q', start_listener)
keyboard.wait('esc')
