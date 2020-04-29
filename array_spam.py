import pyperclip
import pyautogui
import time
import random





def spam():

    with open('spammer.txt', 'r') as file:
        lines = file.read().split(' ')

    print('Initiating Spam Protocol')
    time.sleep(5)

    for item in lines:

        if item != lines[-1]:
            pyperclip.copy(item)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')
            print('Printed : ', item)
            time.sleep(0.5)

        if item == lines[-1]:
            pyperclip.copy(lines[-1])
            print('last digit reached')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')
            print('Printed : ', item)
            time.sleep(3.5)

spam()