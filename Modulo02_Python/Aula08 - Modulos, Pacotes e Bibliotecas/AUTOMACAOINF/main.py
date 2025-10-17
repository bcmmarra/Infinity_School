import time
import pyautogui

pyautogui.press('win')
time.sleep(2)
pyautogui.write('Microsoft Edge')
time.sleep(1)
pyautogui.press('return')
time.sleep(2)

pyautogui.click(x=1572, y=122)