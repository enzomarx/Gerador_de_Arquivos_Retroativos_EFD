import time
import pyautogui

pyautogui.PAUSE = 0.70
time.sleep(3)

# Importação
for _ in range(1000):
    pyautogui.click(x=42, y=69) # clia em icon importr
    time.sleep(3)
    pyautogui.click(x=206, y=217) # Primeiro Arq
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(7)
    pyautogui.press('enter') # validar conteudo
    time.sleep(9)
    pyautogui.press('enter') # ok
    time.sleep(7)
    pyautogui.press('enter') # ok
    time.sleep(5)
    pyautogui.click(x=228, y=69) # X laranja
    time.sleep(1)

    # Lixeira
    pyautogui.click(x=377, y=74) # icon lixo
    time.sleep(2)
    pyautogui.click(x=323, y=339) # seleção
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')                             
    time.sleep(3)
    pyautogui.press('enter')                        
    time.sleep(3)

    # update explorer
    pyautogui.click(x=852, y=67) # update button
    time.sleep(1)
    pyautogui.click(856, 180)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'x')
    time.sleep(1)
    pyautogui.click(x=1003, y=25)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(1003, 25)
    time.sleep(2)

