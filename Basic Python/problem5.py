import pyautogui
from time import sleep

n = int(input())

sleep(5)

pyautogui.write(str(n) + '\n', interval=0.25)

for i in range(1, n+1): 
    str = '#' * i
    pyautogui.write(str + '\n', interval=0.25)

