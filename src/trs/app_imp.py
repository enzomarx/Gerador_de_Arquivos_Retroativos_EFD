import time
import pyautogui

pyautogui.PAUSE = 0.70
time.sleep(1.5)

# Importação
for _ in range(1000):
    pyautogui.click(x=42, y=69) # clia em icon importr
    time.sleep(3)
    pyautogui.click(x=206, y=217) # Primeiro Arq
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter') # validar conteudo
    time.sleep(6)
    pyautogui.press('enter') # ok
    time.sleep(6)
    pyautogui.press('enter') # ok
    time.sleep(3)
    pyautogui.click(x=228, y=69) # X laranja
    time.sleep(1)

    # update explorer
    pyautogui.click(x=852, y=67) # update button
    time.sleep(0.40)
    pyautogui.click(914, 185)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'x')
    time.sleep(1)
    pyautogui.click(x=1003, y=25)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(811, 21)
    time.sleep(2)

