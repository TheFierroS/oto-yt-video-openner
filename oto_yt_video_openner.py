from tkinter.constants import X
import webbrowser
import pyautogui
import time
x = input("Not: Bu Programı Kullanabilmek için ekran çözünürlüğünüz 1920x1080 olmalıdır.\nNot2: Türkçe Karakter Kullanmayın.\nİyi Kullanımlar :)\nAçmak İstediğiniz Videonun İsmini Giriniz : -> ")
webbrowser.open_new("https://www.youtube.com")
time.sleep(2)
pyautogui.moveTo(698,180)
pyautogui.click(button='left', clicks=1, interval=0.25)
pyautogui.typewrite(x, interval=0.05)
pyautogui.moveTo(1283,180)
pyautogui.press("enter")
pyautogui.moveTo(620,420)
time.sleep(1)
pyautogui.click(button='left', clicks=1, interval=0.25)



