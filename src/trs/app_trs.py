import time
import pyautogui

pyautogui.PAUSE = 0.70
time.sleep(3)

# Importação
for _ in range(1051):
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
    
    # Assinatura
    pyautogui.click(x=258, y=73) # icon assin
    time.sleep(2)
    pyautogui.click(x=290, y=338) # seleção
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=269, y=325) # segundo certifi
    time.sleep(2)
    pyautogui.click(x=529, y=478) # ok
    time.sleep(2)
    pyautogui.click(x=328, y=394) # ok

    # Transmissão
    time.sleep(4)
    pyautogui.click(x=319, y=70) # transm icon
    time.sleep(2)
    pyautogui.click(x=326, y=340) # seleção
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.click(x=380, y=427) # nao salvar recibo
    time.sleep(3)

    # Lixeira
    pyautogui.click(x=377, y=74) # icon lixo
    time.sleep(2)
    pyautogui.click(x=323, y=339) # seleção
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')                             #click(x=309, y=395) # sim
    time.sleep(3)
    pyautogui.press('enter')                        #(x=345, y=391) # ok
    time.sleep(3)

    # update explorer
    pyautogui.click(x=852, y=67) # update button
    time.sleep(1)
    pyautogui.moveTo(856, 180)
    time.sleep(1)
    pyautogui.dragTo(1033, 212, duration=1)
    time.sleep(1)
    pyautogui.press('delete')
    time.sleep(2)


