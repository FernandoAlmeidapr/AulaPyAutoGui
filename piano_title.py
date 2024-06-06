# quais são os passos manuais que devo transformar em código
import pyautogui
import keyboard
import win32api
import win32con
import time

#site https://gameforge.com/en-US/littlegames/magic-piano-tiles/#

time.sleep(5)
pyautogui.click(1131,707, duration=1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(888,514, (0, 0, 0)):
        click(888,514)
    if pyautogui.pixelMatchesColor(1056,517, (0, 0, 0)):
        click(1056,517)
    if pyautogui.pixelMatchesColor(1169,526, (0, 0, 0)):
        click(1169,526)
    if pyautogui.pixelMatchesColor(1304,530, (0, 0, 0)):
        click(1304,530)