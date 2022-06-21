import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write('google')
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("youtube.com")
pyautogui.press("enter")
time.sleep(1)

pyautogui.click(x=528, y=338,clicks=3, interval=0.5 )
    
pyautogui.FAILSAFE = True
    



""""
#
time.sleep(4)
x, y = pyautogui.position()
print ("Posicao atual do mouse:")
print ("x = "+str(x)+" y = "+str(y))
#retorna True se x & y estiverem dentro da tela
print ("\nEsta dentro da tela?")
resp = pyautogui.onScreen(x, y)
print (str(resp))"""

"""
while True:
    x, y = pyautogui.position()
    print(f'x: {x}, y: {y}')
    time.sleep(0.3) 
    
"""