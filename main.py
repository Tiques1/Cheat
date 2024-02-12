import keyboard
from pynput.mouse import Listener
import draw_line as dl
import threading


def start_listener():

    def on_click(x, y, button, pressed):
        if pressed:
            dl.mouse_down = True
            threading.Thread(target=dl.line, args=(x, y)).start()
            # print(f'Нажата кнопка {button} в точке: x={x}, y={y}')
        else:
            dl.mouse_down = False
            # print(f'Отпущена кнопка {button} в точке: x={x}, y={y}')
            listener.stop()

    with Listener(on_click=on_click) as listener:
        listener.join()


keyboard.add_hotkey('ctrl+alt+c', start_listener)
keyboard.wait('esc')
