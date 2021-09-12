from tkinter.constants import X
import webbrowser
import pyautogui
import time
def sarkiAc():
    while True:
        print("-"*50)
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
        dongu()
def dongu():
    while True:
        print("-"*50)
        y = input("Çalan Şarkıyı Döngüye Almak İçin 1,\nÇalan Şarkıyı Döngüden Çıkarmak İçin 2,\nYeni Şarkı Açmak İçin 3 ü tuşlayınız -> ")
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
        elif y == "3":
            sarkiAc()
        else:
            print("Hatalı Tuşlama Yaptınız !")
sarkiAc()



