from cgitb import text

import time

#pip install pyautogui
import pyautogui

def sendSpamBot():
    time.sleep(10)

    text = open('SpamMessage.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')


sendSpamBot()
