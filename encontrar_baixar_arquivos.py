'''1) abrir site https://cursoautomacao.netlify.app/
2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
3) Clique em alerta, para gerar a alerta
4) Feche a alerta
5) Suba a página totalmente para cima
6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU" '''

import pyautogui
import time
import webbrowser
#abrir o site
webbrowser.open('https://cursoautomacao.netlify.app')
time.sleep(0.5)
#mover mouse até o centro da pagina
pyautogui.moveTo(4631,735, duration=2)
#rolar a pagina
pyautogui.scroll(-1000)
time.sleep(0.3)
#clicar no campo e digitar o nome
pyautogui.click(5174,419, duration=1)
pyautogui.typewrite("Fernando Almeida")
time.sleep(0.2)
#clicar para exibir o  alerta
pyautogui.click(5085,489, duration=0.2)
time.sleep(0.2)
#Clicar no Alerta para fecha-lo
pyautogui.click(4574,285, duration=0.5)
#rolar a pagina pra cima
pyautogui.scroll(1500)
time.sleep(1)
#descer a pagina até os arquivos para baixar
pyautogui.scroll(-1600)
time.sleep(1)
#clicar em baixar excel
pyautogui.click(3564,972, duration=1)
time.sleep(0.5)
#clicar e baixar pdf
pyautogui.click(3884,975, duration=1)
time.sleep(1)
pyautogui.alert("Você Terminou")

