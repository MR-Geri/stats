from data.keyboard import action_two_key, keyboard_layout

import time
import pygame
import win32api
import win32con


def open_music():
    action_two_key(win32con.VK_LWIN, 0x51)
    keyboard_layout('68748313')
    for ind in [0x5A, 0x59, 0x4C, 0x54, 0x52, 0x43, 0xBF, 0x56, 0x45, 0x50, 0x53, 0x52, 0x46, 0x0D]:
        win32api.keybd_event(ind, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        win32api.keybd_event(ind, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.001)
    time.sleep(0.2)
    win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)


def get_app(path='data/path.txt'):
    """
    Создание кнопок для открытия
    :param path: путь до системного файла
    :return: список всех приложений для кнопок
    """
    apps = []
    with open(path, encoding='utf-8', mode='r') as file:
        data = [
            [i.split('; ') for i in line.split('\n')[1:-1]]
            for line in file.read().split(f'-' * 5)
        ]
        for line_ind in range(len(data)):
            for app_ind in range(len(data[line_ind])):
                if_path = eval(data[line_ind][app_ind][3])
                apps.append(
                    {
                        'name': data[line_ind][app_ind][0],
                        'x': 27 + 60 * app_ind,
                        'y': 355 + 60 * line_ind,
                        'icon': pygame.image.load(data[line_ind][app_ind][1]),
                        'os_open': fr'{data[line_ind][app_ind][2]}' if if_path else eval(data[line_ind][app_ind][2]),
                        'if_os_open_name': if_path
                    }
                )
    return apps


APP = get_app()
