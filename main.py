import pyautogui
import cv2
import time

user_input_theme = input("Choose black theme in DeBank and press ENTER")
startImg = 'img/blackStart.png'
trustImg = 'img/black.png'
user_input = input("Количество Trust: ")
print('Скрипт запустится через 3 секунд, будет поставлено',user_input," Trust")
trust_count = int(user_input)
time.sleep(3)

def main():
    startPosition = pyautogui.locateCenterOnScreen(startImg, confidence=0.99)
    pyautogui.moveTo(startPosition)
    click = 0
    while click < trust_count:
        trust = pyautogui.locateOnScreen(trustImg, confidence=0.9998)
        time.sleep(0.2)
        if trust is None:
            pyautogui.scroll(-700)
            time.sleep(0.2)
        else:
            pyautogui.moveTo(trust, duration=0.5)
            pyautogui.click(trust, button='left')
            click += 1
            print("Trust click", click)
    input("Press ENTER")
if __name__ == '__main__':
    main()
