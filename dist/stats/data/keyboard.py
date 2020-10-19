import time
import win32api
import win32con


def action_two_key(one, two):
    win32api.keybd_event(one, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
    win32api.Sleep(50)
    win32api.keybd_event(two, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
    win32api.Sleep(50)
    win32api.keybd_event(two, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
    win32api.Sleep(50)
    win32api.keybd_event(one, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
    win32api.Sleep(50)


def keyboard_layout(need):
    if str(win32api.GetKeyboardLayout()) != need:
        time.sleep(0.3)
        print('Смена расскладки')
        action_two_key(0x12, 0xA0)
    time.sleep(0.3)
