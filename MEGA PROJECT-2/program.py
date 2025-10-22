import pyautogui
import time
import pyperclip

pyautogui.click(1639,1412)

time.sleep(1)


pyautogui.moveTo(547, 142)
pyautogui.dragTo(1894,1007, duration=1.0,button='left')

pyautogui.hotkey('ctrl','c')
time.sleep(1)

text = pyperclip.paste()

print(text)
