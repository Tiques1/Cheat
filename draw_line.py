import win32gui as wg
import win32api as wa
import pyautogui

mouse_down = True


def line(x1, y1):
    context = wg.GetDC(0)
    color = wa.RGB(35, 255, 0)
    brush = wg.CreateSolidBrush(color)
    wg.SelectObject(context, brush)

    while mouse_down:
        x2, y2 = pyautogui.position()
        wg.MoveToEx(context, x1, y1)
        wg.LineTo(context, x2, y2)

    wg.ReleaseDC(0, context)
    wg.DeleteObject(brush)
