import time
import pyautogui

pyautogui.click(3995,480, duration= 0.3)
pyautogui.write("CMD")
time.sleep(0.2)
pyautogui.press("enter")

for i in range(10):
    pyautogui.write(f"mkdir teste{i}")
    pyautogui.press("enter")
    time.sleep(0.2)
pyautogui.keyDown("ALT")
pyautogui.press("F4")
pyautogui.keyUp("ALT")
time.sleep(0.3)
pyautogui.click(4068,747, duration=1)
pyautogui.keyDown("CTRL")
pyautogui.press("a")
time.sleep(0.2)
pyautogui.keyUp("CTRL")
time.sleep(0.2)
pyautogui.moveTo(4077,696, duration=0.5)
pyautogui.dragTo(5069,771, button="left", duration=1)