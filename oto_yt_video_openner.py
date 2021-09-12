from tkinter.constants import X
import webbrowser
import pyautogui
import time
while True:
    x = input("Not: Bu Programı Kullanabilmek için ekran çözünürlüğünüz 1920x1080 olmalıdır.\nNot2: Türkçe Karakter Kullanmayın.\nİyi Kullanımlar :)\nAçmak İstediğiniz Videonun İsmini Giriniz : -> ")
    webbrowser.open_new("https://www.youtube.com")
    time.sleep(3)
    pyautogui.moveTo(698,180)
    pyautogui.click(button='left', clicks=1, interval=0.25)
    pyautogui.typewrite(x, interval=0.05)
    pyautogui.moveTo(1283,180)
    pyautogui.press("enter")
    pyautogui.moveTo(620,420)
    time.sleep(2)
    pyautogui.click(button='left', clicks=1, interval=0.25)
    y = input("Çalan Şarkıyı Döngüye Almak İçin 1 , Döngüden Çıkarmak için 2 Tuşuna Basınız... ")
    if y == "1":
        pyautogui.moveTo(457,485)
        pyautogui.click(button='right', clicks=1, interval=0.25)
        pyautogui.moveTo(614,519)
        pyautogui.click(button='left', clicks=1, interval=0.25)
    elif y == "2":
        pyautogui.moveTo(457,485)
        pyautogui.click(button='right', clicks=1, interval=0.25)
        pyautogui.moveTo(614,519)
        pyautogui.click(button='left', clicks=1, interval=0.25)
    else:
        print("Hatalı Tuşlama Yaptınız !")



