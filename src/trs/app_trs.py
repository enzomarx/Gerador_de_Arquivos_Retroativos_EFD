import time
import pyautogui

pyautogui.PAUSE = 0.40
time.sleep(3)
# Importação
pyautogui.click(x=42, y=69) # clia em icon importr
pyautogui.click(x=206, y=217) # Primeiro Arq
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=289, y=407) # validar conteudo
time.sleep(6)
pyautogui.click(x=324, y=392) # ok
time.sleep(2)
pyautogui.click(x=324, y=392) # ok
time.sleep(3)
pyautogui.click(x=228, y=69) # X laranja

# Assinatura
pyautogui.click(x=258, y=73) # icon assin
time.sleep(1)
pyautogui.click(x=290, y=338) # seleção
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=269, y=325) # segundo certifi
pyautogui.click(x=529, y=478) # ok
pyautogui.click(x=328, y=394) # ok

# Transmissão
time.sleep(3)
pyautogui.click(x=319, y=70) # transm icon
time.sleep(1)
pyautogui.click(x=326, y=340) # seleção
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=380, y=427) # nao salvar recibo
time.sleep(2)

# Lixeira
pyautogui.click(x=377, y=74) # icon lixo
time.sleep(1)
pyautogui.click(x=323, y=339) # seleção
time.sleep(1)
pyautogui.click(x=309, y=395) # sim
time.sleep(2)
pyautogui.click(x=345, y=391) # ok
time.sleep(2)

# update explorer
pyautogui.click(x=852, y=67) # update button
pyautogui.moveTo(856, 180)
pyautogui.dragTo(1033, 212, duration=1)
pyautogui.press('delete')
time.sleep(1)


