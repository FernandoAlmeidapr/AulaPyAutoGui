import pyautogui
captcha = pyautogui.locateCenterOnScreen("captcha.png")
pyautogui.click(captcha[0], captcha[1])