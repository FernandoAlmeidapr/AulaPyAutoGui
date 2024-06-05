import time
import pyautogui

usuario = pyautogui.prompt("Informe Seu Usuário", title="Automação")
senha = pyautogui.password("Informe Sua Senha", title="Aula DevAprender", mask='*')
time.sleep(0.3)
pyautogui.hotkey("winleft", "r")
time.sleep(0.2)
pyautogui.typewrite("notepad")
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.moveTo(4536,644, duration=1)
pyautogui.typewrite(f"{usuario}|{senha}")