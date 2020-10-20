from data.drawing import print_text, draw_disk, draw_time, draw_statistic
from data.keyboard import keyboard_layout
from data.run_line import run_line
from data.voice import take_a_break
from data.apps_open import APP, open_music
from data.temperature import temperatures
import os
from threading import Thread
import psutil
import datetime

import pygame
import win32gui


inf = {"CPU": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       "RAM": [16329, 0, 0, 0],
       "Диск C": [90.4, 0, 0, 0],
       "Диск D": [374.81, 0, 0, 0],
       "Диск G": [250.34, 0, 0, 0],
       "Диск F": [430.52, 0, 0, 0],
       "Диск H": [250.65, 0, 0, 0],
       "Диск E": [931.51, 0, 0, 0],
       "time": [12, 11, 57, 00]}
last_active_windows = ''
time_of_the_las_passage = datetime.datetime.now()
reminder_time = datetime.datetime.now()
tim = 0
last = 0
last_r = 0
block_run = 0
ind_run = 0
vl_list_run = 0
CPU_CHART = True
GPU_CHART = True
RAM_CHART = True
T_CPU_CHART = True
T_GPU_CHART = True
timer = pygame.time.Clock()
os.environ['SDL_VIDEO_WINDOW_POS'] = '-1080, 1617'
pygame.init()
display = pygame.display.set_mode((1080, 480))
pygame.display.set_caption("Stats")
pygame.display.set_icon(pygame.image.load("data/icon/stats.ico"))


def info():
    """  Загруженносить системы. """
    global inf
    # Ram: Всего, Доступно, Использовано (мб), Проценты
    # Диски: Всего, Использовано, Доступно (гб), Процент
    # считываний, записей, прочитано мб, записано мб, чтение сек, запись сек.
    while True:
        times = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
        inf = {
            'CPU': psutil.cpu_percent(interval=1, percpu=True),
            'RAM': [int(i / 1024 / 1024) if i > 101 else int(i) for i in psutil.virtual_memory()],
            'time': [times.days, times.seconds // 3600, (times.seconds % 3600) // 60, (times.seconds % 3600) % 60]
        }
        for i in 'CDGFHE':
            disk = [i / 1024 / 1024 / 1024 if i > 101 else i for i in psutil.disk_usage(f'{i}:\\')]
            inf[f'Диск {i}'] = [float('{:.2f}'.format(disk[0])), float('{:.2f}'.format(disk[1])),
                                float('{:.2f}'.format(disk[2])), int(disk[3])]


def drawing():
    """Вывод всей информации на экран"""

    def changing_the_language():
        global last_active_windows
        active_windows = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if last_active_windows != active_windows and active_windows == 'WhatsApp':
            keyboard_layout('68748313')
        last_active_windows = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    def click_button(running_line):
        global last, last_r, CPU_CHART, GPU_CHART, RAM_CHART, T_CPU_CHART, T_GPU_CHART, block_run, ind_run, vl_list_run
        mouse, click, click_r = pygame.mouse.get_pos(), pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2]
        # Показ CPU графика
        if 502 < mouse[0] < 522 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            CPU_CHART = False if CPU_CHART else True
        if 522 < mouse[0] < 542 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            GPU_CHART = False if GPU_CHART else True
        if 542 < mouse[0] < 562 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            RAM_CHART = False if RAM_CHART else True
        if 562 < mouse[0] < 597 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            T_CPU_CHART = False if T_CPU_CHART else True
        if 597 < mouse[0] < 632 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            T_GPU_CHART = False if T_GPU_CHART else True
        if 478 < mouse[0] < 500 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            CPU_CHART, GPU_CHART, RAM_CHART, T_CPU_CHART, T_GPU_CHART = False, False, False, False, False
        if 25 < mouse[0] < 25 + 48 and 137 + 48 > mouse[1] > 137 and click == 1 and last == 0:
            block_run = 0 if block_run == len(running_line) - 1 else block_run - 1
            ind_run = 0
            vl_list_run = 0
        if 400 < mouse[0] < 400 + 48 and 137 + 48 > mouse[1] > 137 and click == 1 and last == 0:
            block_run = 0 if block_run == len(running_line) - 1 else block_run + 1
            ind_run = 0
            vl_list_run = 0
        if 25 + 48 < mouse[0] < 400 and 137 + 48 > mouse[1] > 137 and click == 1 and last == 0:
            ind_run = 0 if ind_run == len(running_line[block_run][vl_list_run][0]) - 1 else ind_run + 1
        if 25 + 48 < mouse[0] < 400 and 137 + 48 > mouse[1] > 137 and click_r == 1 and last_r == 0:
            vl_list_run = 0 if vl_list_run == len(running_line[block_run]) - 1 else vl_list_run + 1
            ind_run = 0
        # Открытие приложений
        for app in APP:
            if app['x'] + 60 > mouse[0] > app['x'] and app['y'] + 60 > mouse[1] > app['y'] \
                    and click == 1 and last == 0:
                print('Открытие', app['name'])
                if app['if_os_open_name']:
                    os.system("start " + app['os_open'])
                else:
                    app['os_open']()
        last = 0 if pygame.mouse.get_pressed()[0] == 0 else 1
        last_r = 0 if pygame.mouse.get_pressed()[2] == 0 else 1

    def blit_all_rect():
        pygame.draw.rect(display, (50, 51, 50), (770, 10, 300, 330))
        pygame.draw.rect(display, (128, 128, 128), (780, 20, 280, 100))
        pygame.draw.rect(display, (128, 128, 128), (780, 125, 280, 100))
        pygame.draw.rect(display, (50, 51, 50), (460, 10, 300, 330))
        pygame.draw.rect(display, (128, 128, 128), (470, 20, 280, 100))
        pygame.draw.rect(display, (128, 128, 128), (470, 125, 280, 100))
        pygame.draw.rect(display, (128, 128, 128), (470, 230, 280, 100))
        pygame.draw.rect(display, (128, 128, 128), (780, 230, 280, 100))
        pygame.draw.rect(display, (50, 51, 50), (10, 10, 440, 330))
        #
        pygame.draw.rect(display, (50, 51, 50), (10, 350, 750, 120))
        # отрисовка приложений
        for app in APP:
            display.blit(app['icon'], (int(app['x']), int(app['y'])))

    # Ram: Всего, Доступно, Использовано (мб), Проценты
    # Диски: Всего, Использовано, Доступно (гб), Процент
    # считываний, записей, прочитано мб, записано мб, чтение сек, запись сек.
    global time_of_the_las_passage, CPU_CHART, GPU_CHART, RAM_CHART, T_CPU_CHART, T_GPU_CHART, \
        block_run, ind_run, vl_list_run, reminder_time
    info_thread = Thread(target=info)
    info_thread.start()
    running_line = run_line()
    while True:
        timer.tick(60)
        display.fill((0, 0, 0))
        click_button(running_line)
        changing_the_language()
        now_time = datetime.datetime.now()
        update_time = now_time - time_of_the_las_passage
        if (now_time - reminder_time).seconds // 1800 >= 1:
            print('Обновление информации бегущей строки и напоминание.')
            reminder_time = now_time
            take_a_break()
            running_line = run_line()
        if int(update_time.seconds) + int(str(update_time.microseconds)[:2]) / 100 >= 1:
            blit_all_rect()
            temp = temperatures()
            # блок времени
            draw_time(display, inf)
            if not CPU_CHART and not GPU_CHART and not RAM_CHART and not T_CPU_CHART and not T_GPU_CHART:
                draw_disk(display, inf)
            # Бегущая строка
            pygame.draw.rect(display, (128, 128, 128), (20, 20, 420, 100))
            pygame.draw.rect(display, (128, 128, 128), (20, 130, 420, 200))
            display.blit(pygame.image.load('data/button_left.png'), (25, 137))
            display.blit(pygame.image.load('data/button_right.png'), (400, 137))
            print_text(display, *running_line[block_run][vl_list_run][0][ind_run],
                       font_color=running_line[block_run][vl_list_run][1])
            #
            draw_statistic(display, inf, temp, CPU_CHART, GPU_CHART, RAM_CHART, T_CPU_CHART, T_GPU_CHART)
            pygame.display.update()
            time_of_the_las_passage = datetime.datetime.now()
        for en in pygame.event.get():
            if en.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == '__main__':
    drawing()
