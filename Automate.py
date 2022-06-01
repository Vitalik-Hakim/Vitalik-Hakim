import pyautogui
import tkinter
import time
import string



subjects = []



# pyautogui.click()          # Click the mouse.
pyautogui.click(110, 10)  # Click Web browser tab
# pyautogui.hotkey('ctrl', 'f')
# pyautogui.write('abubakar', interval=0)
# pyautogui.press('esc')
# with pyautogui.hold('shift'):
#       # Press the Shift key down and hold it.
#     pyautogui.press(['right', 'right', 'right', 'right'])
r = 7 # init cell A and G with 7
for G in range(80):
    pyautogui.click(110, 10) 
    r = r+6 # Increase cell A and G selection by 6.
    rs = str(r)
    pyautogui.click(32, 185) # Open Cell input window
    pyautogui.hotkey('ctrl', 'x')
    pyautogui.press('backspace')
    clipboard_content = tkinter.Tk().clipboard_get()
    new_k = "A" + rs
    new_c = ":G"
    new_all = new_k + new_c 
    new_content =   new_all + rs 
    # new content will be selection of Name with courses and grades
    pyautogui.write(new_content, interval=0)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(352, 0)
    #Send data to second chrome tab
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(84, 274)
    # Copy name and find surname
    pyautogui.hotkey('ctrl', 'c')
    clip_name = tkinter.Tk().clipboard_get()
    surname = clip_name.split(" ")
    surname_clean = surname[1]
    # surname_clean = surname_clean.replace("(DIPLOMA)","")
    surname_clean = surname_clean.rstrip()
    # full_name = clip_name.rstrip()
    # clean_name = full_name.replace("-","")
    print(surname_clean)
    # Copy subjects and final grade
    pyautogui.press(['tab', 'tab', 'tab'])
    pyautogui.hotkey('ctrl', 'c')
    clip_subject = tkinter.Tk().clipboard_get()
    pyautogui.press(['tab', 'tab'])
    pyautogui.hotkey('ctrl', 'c')
    clip_finalgrade = tkinter.Tk().clipboard_get()
    print(clip_finalgrade)
    #Open third chrome tab and 
    pyautogui.click(584, 12)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write(clip_subject, interval=0)
    time.sleep(2)
    pyautogui.press('esc')
    pyautogui.press('esc')
    while True:
        pyautogui.press('down')
        pyautogui.hotkey('ctrl', 'c')
        clip_newname = tkinter.Tk().clipboard_get()
        print(clip_newname,surname_clean)
        cliplen = len(clip_newname)
        print(cliplen)
        if surname_clean in clip_newname:
            print("passed")
            pyautogui.press(['tab', 'tab', 'tab'])
            pyautogui.write(clip_finalgrade, interval=0)
            break
        elif cliplen == 1:
            break
        else:
            print("failed")
            pass
        time.sleep(1)
    pyautogui.click(110, 10)









# 000709 0002 (hjm140) Libelo, Yohannes Gebremeskel
# 000709 0002 (hjm140)  Libelo ,Yohannes Gebremeskel

# pyautogui.hotkey('ctrl', 'c')
# pyautogui.click(352, 0)
# pyautogui.hotkey('ctrl', 'f')
# pyautogui.write('abubakar', interval=0)
# pyautogui.press('esc')
# for i in range(0,5):
#     pyautogui.press('tab')
# pyautogui.press('enter')
# pyautogui.hotkey('ctrl', 'v')
