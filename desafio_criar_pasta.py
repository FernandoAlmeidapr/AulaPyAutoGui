import pyautogui
import time

pyautogui.click(3350,375, button="right", duration=0.5)
pyautogui.move(20,505, duration=1)
time.sleep(0.2)
pyautogui.move(450,0, duration=1)
time.sleep(0.2)
pyautogui.click()
time.sleep(0.5)
pyautogui.write("Desafio de Payautogui")
time.sleep(0.1)
pyautogui.press("enter")