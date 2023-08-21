import pyautogui
import time

word = "Text"

while True:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(10)