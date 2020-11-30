import pyautogui
import time

message = "Mabar aja lah pusing"
n = 100

time.sleep(3)

for i in range(n):
    pyautogui.typewrite(message + '\n')
