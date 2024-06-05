import pyautogui
import time

#Clicando nas cordenadas do botão "play"
pyautogui.click(4344,846, duration=0.5)
time.sleep(3.5) #tempo pra carregar a pagina
#clicando no "START"
pyautogui.click()
time.sleep(8.5) #Aguardando carregar
#clicando no botão fechar (popup)
pyautogui.click(4407,830, duration=0.5)
#Posicionando o mouse sobre a pedra
pyautogui.moveTo(4031,693, duration=0.5)
#Clicando 100x
for i in range(100):
    pyautogui.click(duration=0.1)