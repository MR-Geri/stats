## stats
h = win32gui.FindWindow(0, "Info")-окно

win32gui.ShowWindow(h, win32con.SW_MINIMIZE)-свернуть окно

win32gui.SetForegroundWindow(handle) - открыть окно

# Для создания exe в консоль напишите:
pyinstaller --icon=stats.ico -y stats.py 

После запустите loader.py
