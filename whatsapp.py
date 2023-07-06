
import pywhatkit
import pyautogui
import keyboard
#pyautogui.click(x=741, y=71)
#pywhatkit.sendwhatmsg_to_group_instantly("JOGa8NPcKISK6myhQHC0W6", "testing", tab_close = True, close_time = 2)

def sendwhatmsg(phone_number, message):
    #pywhatkit.sendwhatmsg("+852 6609 6066", 'Message 1', 12,22, wait_time = 10, tab_close = True, close_time = 2)
    pywhatkit.sendwhatmsg_instantly(phone_number, message, tab_close = True, close_time = 2)
    
def sendwhatmsg_to_group(group_code = "JOGa8NPcKISK6myhQHC0W6", message = "testing"):
    #trash grp:JOGa8NPcKISK6myhQHC0W6
    #fam: GPZpNoHuLGWEbmBwSwzyjD
    #pywhatkit.sendwhatmsg_to_group_instantly("JOGa8NPcKISK6myhQHC0W6", "testing", tab_close = True, close_time = 2)
    pywhatkit.sendwhatmsg_to_group_instantly(group_code, message, tab_close = True, close_time = 2)
    #keyboard.send('enter')