import time
import pyautogui
import pyperclip

#Função para uso do Pyperclip
def escrever_texto(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")


pyautogui.keyDown("winleft")
pyautogui.press("r")
time.sleep(0.5)
pyautogui.keyUp("winleft")
pyautogui.write("notepad")
pyautogui.press("enter")
time.sleep(1)
pyautogui.moveTo(4347,591, duration=1)
escrever_texto("Automação é Incrível")