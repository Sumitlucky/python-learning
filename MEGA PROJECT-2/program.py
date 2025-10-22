import pyautogui
import time
import pyperclip

pyautogui.click(1639,1412)

time.sleep(1)


pyautogui.moveTo(1003, 237)
pyautogui.dragTo(2187,1258, duration=1.0,button='left')

pyautogui.hotkey('ctrl','c')
time.sleep(1)

text = pyperclip.paste()

print(text)
