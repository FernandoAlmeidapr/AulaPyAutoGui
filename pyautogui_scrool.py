import time
import pyautogui

pyautogui.tripleClick(3771,95, duration=1)
time.sleep(0.5)
pyautogui.press("backspace")
time.sleep(0.2)
pyautogui.write("https://pt.wikipedia.org/wiki/Brasil")
time.sleep(0.2)
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.move(0,600)
time.sleep(0.5)
pyautogui.scroll(-2010)