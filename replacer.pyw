
import keyboard
import pyperclip
import time

en = "`qwertyuiop[]asdfghjkl;'zxcvnm,./H"
ar = "ذضصثقفغعهخحجدشسيبلاتنمكطئءؤرىةوزظأ"
running = False

#########################################
replace_all ="ctrl+]" #اختصار تحويل الكل
replace_selected ="ctrl+[" #اختصار تحويل المحدد
#########################################
def replace_selected_text():
    global running
    if running:
        return
    running = True
    
    
    keyboard.press_and_release("ctrl+x")
    time.sleep(0.1)
    text = pyperclip.paste()
    if text and text !="":
        new =""
        for i in text:
            if en.find(i) != -1:
                new += ar[en.find(i)]
            elif ar.find(i) != -1:
                new += en[ar.find(i)]
            else:
                new += i
        pyperclip.copy(new)
        time.sleep(0.1)
        keyboard.press_and_release("ctrl+v")
    running = False

def replace_all_text():
    global running
    if running:
        return
    running = True
    keyboard.press_and_release("ctrl+a")
    time.sleep(0.1)
    keyboard.press_and_release("ctrl+x")
    time.sleep(0.1)
    text = pyperclip.paste()
    if text and text !="":
        new =""
        for i in text:
            if en.find(i) != -1:
                new += ar[en.find(i)]
            elif ar.find(i) != -1:
                new += en[ar.find(i)]
            else:
                new += i
        pyperclip.copy(new)
        time.sleep(0.1)
        keyboard.press_and_release("ctrl+v")
    running = False

keyboard.add_hotkey(replace_selected, replace_selected_text)
keyboard.add_hotkey(replace_all, replace_all_text)
print("started")
keyboard.wait()

