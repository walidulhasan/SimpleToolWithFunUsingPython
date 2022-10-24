import pyautogui
import time
i=1
comments="."

time.sleep(1)
while i < 1000000:
    pyautogui.typewrite(comments)
    pyautogui.typewrite("\n")
    i += 1
    
    
    
