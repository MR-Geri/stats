import datetime
import json
import os
import time
from threading import Thread

import GPUtil
import clr
import plotly.graph_objs as go
import psutil
import pygame
import win32api
import win32com.client
import win32con
import win32gui
from PIL import Image


def keyboard_layout(need):
    if str(win32api.GetKeyboardLayout()) != need:
        time.sleep(0.3)
        print('Смена расскладки')
        action_two_key(0x12, 0xA0)
    time.sleep(0.3)


def open_music():
    action_two_key(win32con.VK_LWIN, 0x51)
    keyboard_layout('68748313')
    for ind in [0x5A, 0x59, 0x4C, 0x54, 0x52, 0x43, 0xBF, 0x56, 0x45, 0x50, 0x53, 0x52, 0x46, 0x0D]:
        win32api.keybd_event(ind, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        win32api.keybd_event(ind, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.001)
    time.sleep(0.3)
    shell.SendKeys('{ENTER}')


APP = [
    {
        'name': 'Pycharm',
        'x': 27,
        'y': 355,
        'icon': pygame.image.load('data/icon/pycharm.png'),
        'os_open': r'D:\PyCharm 2020.1\bin\pycharm64.exe',
        'if_os_open_name': True
    },
    {
        'name': 'Discord',
        'x': 27 + 60,
        'y': 355,
        'icon': pygame.image.load('data/icon/discord.png'),
        'os_open': r'C:\Users\ilyak\AppData\Local\Discord\app-0.0.307\Discord.exe',
        'if_os_open_name': True
    },
    {
        'name': 'Фотошоп',
        'x': 27 + 60 * 4,
        'y': 355,
        'icon': pygame.image.load('data/icon/photoshop.png'),
        'os_open': r'D:\Adobe\Adobe Photoshop CC 2019\Photoshop.exe',
        'if_os_open_name': True
    },
    {
        'name': 'Computer',
        'x': 27 + 60 * 5,
        'y': 355,
        'icon': pygame.image.load('data/icon/computer.png'),
        'os_open': r'C:\Users\ilyak\Desktop\Этот компьютер.lnk',
        'if_os_open_name': True
    },
    {
        'name': 'Project',
        'x': 27 + 60 * 6,
        'y': 355,
        'icon': pygame.image.load('data/icon/project.png'),
        'os_open': r'C:\Users\ilyak\PycharmProjects',
        'if_os_open_name': True
    },
    {
        'name': 'Яндекс Музыка',
        'x': 27,
        'y': 355 + 60,
        'icon': pygame.image.load('data/icon/music.png'),
        'os_open': open_music,
        'if_os_open_name': False
    },
    {
        'name': 'Яндекс Диск',
        'x': 27 + 60,
        'y': 355 + 60,
        'icon': pygame.image.load('data/icon/yandex_disk.png'),
        'os_open': r'C:\Users\ilyak\AppData\Roaming\Yandex\YandexDisk2\3.1.22.3711\YandexDisk2.exe',
        'if_os_open_name': True
    },
    {
        'name': 'WhatsApp',
        'x': 27 + 60 * 2,
        'y': 355 + 60,
        'icon': pygame.image.load('data/icon/whatsapp.png'),
        'os_open': r'C:\Users\ilyak\AppData\Local\WhatsApp\WhatsApp.exe',
        'if_os_open_name': True
    },
    {
        'name': 'Premiere Pro',
        'x': 27 + 60 * 4,
        'y': 355 + 60,
        'icon': pygame.image.load('data/icon/premiere-pro.png'),
        'os_open': r'D:\Adobe\Adobe Premiere Pro 2020\Adobe Premiere Pro.exe',
        'if_os_open_name': True
    },
    {
        'name': 'Download',
        'x': 27 + 60 * 5,
        'y': 355 + 60,
        'icon': pygame.image.load('data/icon/download.png'),
        'os_open': r'C:\Users\ilyak\Downloads',
        'if_os_open_name': True
    },
]
last_active_windows = ''
time_of_the_las_passage = datetime.datetime.now()
tim = 0
last = 0
CPU_CHART = True
GPU_CHART = True
RAM_CHART = True
T_CPU_CHART = True
T_GPU_CHART = True
timer = pygame.time.Clock()
shell = win32com.client.Dispatch("WScript.Shell")
os.environ['SDL_VIDEO_WINDOW_POS'] = '-1080, 1617'
pygame.init()
display = pygame.display.set_mode((1080, 480))
pygame.display.set_caption("Stats")
inf_except = {"CPU": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              "RAM": [16329, 0, 0, 0],
              "Диск C": [90.4, 0, 0, 0],
              "Диск D": [374.81, 0, 0, 0],
              "Диск G": [250.34, 0, 0, 0],
              "Диск F": [430.52, 0, 0, 0],
              "Диск H": [250.65, 0, 0, 0],
              "Диск E": [931.51, 0, 0, 0],
              "time": [12, 11, 57]}
v_tem_1 = ['SYS', 'PCH', 'CPU_GP', 'PCI_E', 'VRM', 'AUX']
v_tem_2 = ['GPU', 'HDD 1', 'HDD 2']
temperature = {}
dll_file_name = os.path.abspath(os.path.dirname(__file__)) + R'\data\OpenHardwareMonitorLib.dll'
clr.AddReference(dll_file_name)
from OpenHardwareMonitor import Hardware

handle = Hardware.Computer()
handle.MainboardEnabled = handle.CPUEnabled = handle.GPUEnabled = handle.HDDEnabled = True
handle.Open()


def print_text(message, x, y, font_color=(255, 255, 255), font_type='data/shrift.otf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


def action_two_key(one, two):
    win32api.keybd_event(one, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
    win32api.Sleep(50)
    win32api.keybd_event(two, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
    win32api.Sleep(50)
    win32api.keybd_event(two, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
    win32api.Sleep(50)
    win32api.keybd_event(one, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
    win32api.Sleep(50)


def info():
    global tim
    # Ram: Всего, Доступно, Использовано (мб), Проценты
    # Диски: Всего, Использовано, Доступно (гб), Процент
    # считываний, записей, прочитано мб, записано мб, чтение сек, запись сек.
    while True:
        t = datetime.datetime.now().strftime("%H:%M:%S").split(':')
        tim = 24 if t[0] == '00' and tim == 0 else tim
        t[0] = str(int(t[0]) + tim)
        t1 = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M:%S").split(':')
        t = (int(t[0]) - int(t1[0])) * 3600 + (int(t[1]) - int(t1[1])) * 60 + int(t[2]) - int(t1[2])
        inf = {
            'CPU': psutil.cpu_percent(interval=1, percpu=True),
            'RAM': [int(i / 1024 / 1024) if i > 101 else int(i) for i in psutil.virtual_memory()],
            'time': [t // 3600, t % 3600 // 60, t % 3600 % 60]
        }
        for i in 'CDGFHE':
            disk = [i / 1024 / 1024 / 1024 if i > 101 else i for i in psutil.disk_usage(f'{i}:\\')]
            inf[f'Диск {i}'] = [float('{:.2f}'.format(disk[0])), float('{:.2f}'.format(disk[1])),
                                float('{:.2f}'.format(disk[2])), int(disk[3])]
        try:
            with open("data/data.json", "w") as write_file:
                json.dump(inf, write_file)
        except:
            print('Была ошибка в записи информации')


def temperatures():

    """Считывание температуры с датчиков"""

    handle.Hardware[0].SubHardware[0].Update()
    for i in v_tem_1:
        ind = v_tem_1.index(i) + 13
        temperature[i] = int(handle.Hardware[0].SubHardware[0].Sensors[ind].Value)
    handle.Hardware[1].Update()
    temperature['CPU'] = [int(handle.Hardware[1].Sensors[i].Value) for i in range(7, 14)]
    for i in v_tem_2:
        ind = v_tem_2.index(i) + 2
        handle.Hardware[ind].Update()
        temperature[i] = int(handle.Hardware[ind].Sensors[0].Value)
    return temperature


def drawing():

    """Вывод всей информации на экран"""

    def changing_the_language():
        global last_active_windows
        active_windows = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if last_active_windows != active_windows and active_windows == 'WhatsApp':
            print('WhatsApp')
            keyboard_layout('68748313')
        last_active_windows = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    def click_button():
        global last, CPU_CHART, GPU_CHART, RAM_CHART, T_CPU_CHART, T_GPU_CHART
        mouse, click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()[0]
        # Показ CPU графика
        if 483 < mouse[0] < 503 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            CPU_CHART = False if CPU_CHART else True
        if 503 < mouse[0] < 523 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            GPU_CHART = False if GPU_CHART else True
        if 523 < mouse[0] < 543 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            RAM_CHART = False if RAM_CHART else True
        if 543 < mouse[0] < 578 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            T_CPU_CHART = False if T_CPU_CHART else True
        if 578 < mouse[0] < 613 and 40 > mouse[1] > 13 and click == 1 and last == 0:
            T_GPU_CHART = False if T_GPU_CHART else True
        # Открытие приложений
        for app in APP:
            if app['x'] + 60 > mouse[0] > app['x'] and app['y'] + 60 > mouse[1] > app['y']\
                    and click == 1 and last == 0:
                print('Открытие', app['name'])
                if app['if_os_open_name']:
                    os.startfile(app['os_open'])
                else:
                    app['os_open']()
        last = 0 if pygame.mouse.get_pressed()[0] == 0 else 1

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
        # первая строка
        for index in APP:
            display.blit(index['icon'], (int(index['x']), int(index['y'])))

    def load_colors(stats):
        if stats < 25:
            return 34, 139, 34
        elif stats < 50:
            return 102, 0, 255
        elif stats < 75:
            return 102, 102, 0
        return 255, 36, 0
    # Ram: Всего, Доступно, Использовано (мб), Проценты
    # Диски: Всего, Использовано, Доступно (гб), Процент
    # считываний, записей, прочитано мб, записано мб, чтение сек, запись сек.
    global time_of_the_las_passage, CPU_CHART, GPU_CHART, RAM_CHART, T_CPU_CHART, T_GPU_CHART
    chart_time_list = [i for i in range(1, 61)]
    chart_cpu_list = []
    chart_gpu_list = []
    chart_ram_list = []
    chart_cpu_temperature_list = []
    chart_gpu_temperature_list = []
    info_thread = Thread(target=info)
    info_thread.start()
    while True:
        timer.tick(60)
        display.fill((0, 0, 0))
        click_button()
        changing_the_language()
        if int(str(datetime.datetime.now() - time_of_the_las_passage)[5:7]) >= 1:
            try:
                inf = json.load(open('data/data.json'))
            except:
                inf = inf_except
                print('Была ошибка в считывании информации')

            blit_all_rect()
            temp = temperatures()
            # блок времени
            pygame.draw.rect(display, (50, 51, 50), (770, 350, 300, 120))
            print_text(f'{datetime.datetime.now().strftime("%H:%M")}', 782, 350, font_size=100)
            print_text(f'{datetime.datetime.now().strftime("%d-%m-%Y")} '
                       + str(inf['time'][0]) + ':' + str(inf['time'][1]), 790, 440)
            if not CPU_CHART and not GPU_CHART and not RAM_CHART and not T_CPU_CHART and not T_GPU_CHART:
                # Блок инфы дисков Правый
                pygame.draw.rect(display, (54, 35, 8), (785, 25, 270, 90))
                pygame.draw.rect(display, (102, 102, 0), (785, 25, int(270 / 100 * int(inf['Диск D'][3])), 90))
                #
                print_text('D: ' + str(inf['Диск D'][0]) + '/GB/', 790, 27, font_size=28)
                print_text('USE: ' + str(inf['Диск D'][1]) + '/GB/', 790, 57, font_size=28)
                print_text('FREE: ' + str(inf['Диск D'][2]) + '/GB/', 790, 87, font_size=28)
                print_text(str(inf['Диск D'][3]) + '%', 1000, 27, font_size=28)

                # Обновляется
                pygame.draw.rect(display, (54, 35, 8), (785, 130, 270, 90))
                pygame.draw.rect(display, (102, 102, 0), (785, 130, int(270 / 100 * int(inf['Диск F'][3])), 90))
                #
                print_text('F: ' + str(inf['Диск F'][0]) + '/GB/', 790, 132, font_size=28)
                print_text('USE: ' + str(inf['Диск F'][1]) + '/GB/', 790, 162, font_size=28)
                print_text('FREE: ' + str(inf['Диск F'][2]) + '/GB/', 790, 192, font_size=28)
                print_text(str(inf['Диск F'][3]) + '%', 1000, 132, font_size=28)
                # Обновляется
                pygame.draw.rect(display, (54, 35, 8), (785, 235, 270, 90))
                pygame.draw.rect(display, (102, 102, 0), (785, 235, int(270 / 100 * int(inf['Диск E'][3])), 90))
                #
                print_text('E: ' + str(inf['Диск E'][0]) + '/GB/', 790, 237, font_size=28)
                print_text('USE: ' + str(inf['Диск E'][1]) + '/GB/', 790, 267, font_size=28)
                print_text('FREE: ' + str(inf['Диск E'][2]) + '/GB/', 790, 297, font_size=28)
                print_text(str(inf['Диск E'][3]) + '%', 1000, 237, font_size=28)
                # Обновляется
                pygame.draw.rect(display, (54, 35, 8), (475, 25, 270, 90))
                pygame.draw.rect(display, (102, 102, 0), (475, 25, int(270 / 100 * int(inf['Диск C'][3])), 90))
                #
                print_text('C: ' + str(inf['Диск C'][0]) + '/GB/', 480, 27, font_size=28)
                print_text('USE: ' + str(inf['Диск C'][1]) + '/GB/', 480, 57, font_size=28)
                print_text('FREE: ' + str(inf['Диск C'][2]) + '/GB/', 480, 87, font_size=28)
                print_text(str(inf['Диск C'][3]) + '%', 690, 27, font_size=28)
                # Обновляется
                pygame.draw.rect(display, (54, 35, 8), (475, 130, 270, 90))
                pygame.draw.rect(display, (102, 102, 0), (475, 130, int(270 / 100 * int(inf['Диск G'][3])), 90))
                #
                print_text('G: ' + str(inf['Диск G'][0]) + '/GB/', 480, 132, font_size=28)
                print_text('USE: ' + str(inf['Диск G'][1]) + '/GB/', 480, 162, font_size=28)
                print_text('FREE: ' + str(inf['Диск G'][2]) + '/GB/', 480, 192, font_size=28)
                print_text(str(inf['Диск G'][3]) + '%', 690, 132, font_size=28)
                # Обновляется
                pygame.draw.rect(display, (54, 35, 8), (475, 235, 270, 90))
                pygame.draw.rect(display, (102, 102, 0), (475, 235, int(270 / 100 * int(inf['Диск H'][3])), 90))
                #
                print_text('H: ' + str(inf['Диск H'][0]) + '/GB/', 480, 237, font_size=28)
                print_text('USE: ' + str(inf['Диск H'][1]) + '/GB/', 480, 267, font_size=28)
                print_text('FREE: ' + str(inf['Диск H'][2]) + '/GB/', 480, 297, font_size=28)
                print_text(str(inf['Диск H'][3]) + '%', 690, 237, font_size=28)
            #
            pygame.draw.rect(display, (128, 128, 128), (20, 20, 420, 100))
            pygame.draw.rect(display, (128, 128, 128), (20, 130, 420, 200))
            #
            print_text('AUX-{0} CGP-{1} SYS-{2}'.format(temp['AUX'], temp['CPU_GP'], temp['SYS']),
                       55, 40, font_size=30)
            print_text('PCH-{0} PCI-{1} VRM-{2}'.format(temp['PCH'], temp['PCI_E'], temp['VRM']),
                       55, 75, font_size=30)

            print_text('Какой-то текст потом', 55, 60 + 40 * 2, font_size=30)
            # Обновляется CPU
            cpu = int(sum(inf['CPU']) / 12)
            z = 4 * cpu
            pygame.draw.rect(display, (54, 35, 8), (30, 55 + 40 * 3, 400, 33))
            pygame.draw.rect(display, load_colors(cpu), (30, 55 + 40 * 3, z, 33))
            # Обновляется GPU
            gp = GPUtil.getGPUs()[0]
            gpu = int(gp.load * 100)
            z = 4 * gpu
            pygame.draw.rect(display, (54, 35, 8), (30, 55 + 40 * 4, 400, 33))
            pygame.draw.rect(display, load_colors(gpu), (30, 55 + 40 * 4, z, 33))
            # Обновляется RAM
            z = 4 * inf['RAM'][2]
            pygame.draw.rect(display, (54, 35, 8), (30, 55 + 40 * 5, 400, 33))
            pygame.draw.rect(display, load_colors(inf['RAM'][2]), (30, 55 + 40 * 5, z, 33))
            cp = str(sum([int(i) for i in temp['CPU']]) // 7)
            print_text('CPU-' + cp + ' (' + f"{cpu}%) Core-" + str(temp['CPU'][-1]), 32, 58 + 40 * 3, font_size=30)
            print_text('GPU-' + str(temp['GPU']) + ' (' + f"{gpu}%) " + f"{int(gp.memoryFree)}MB",
                       32, 58 + 40 * 4, font_size=30)
            print_text('RAM-' + str(inf['RAM'][0]) + 'MB        ' + str(inf['RAM'][2]) + '%',
                       32, 58 + 40 * 5, font_size=30)
            print_text('use-' + str(inf['RAM'][3]) + 'MB free-' + str(inf['RAM'][1]) + 'MB',
                       35, 58 + 40 * 6, font_size=30)
            if CPU_CHART or GPU_CHART or RAM_CHART or T_CPU_CHART or T_GPU_CHART:
                if len(chart_cpu_list) >= len(chart_time_list):
                    chart_cpu_list = chart_cpu_list[1:]
                if len(chart_gpu_list) >= len(chart_time_list):
                    chart_gpu_list = chart_gpu_list[1:]
                if len(chart_ram_list) >= len(chart_time_list):
                    chart_ram_list = chart_ram_list[1:]
                if len(chart_cpu_temperature_list) >= len(chart_time_list):
                    chart_cpu_temperature_list = chart_cpu_temperature_list[1:]
                if len(chart_gpu_temperature_list) >= len(chart_time_list):
                    chart_gpu_temperature_list = chart_gpu_temperature_list[1:]
                chart_cpu_list.append(cpu)
                chart_gpu_list.append(gpu)
                chart_ram_list.append(inf['RAM'][2])
                chart_cpu_temperature_list.append(cp)
                chart_gpu_temperature_list.append(temp['GPU'])
                fig = go.Figure(layout=go.Layout(plot_bgcolor='rgb(128, 128, 128)',
                                                 paper_bgcolor='rgb(50, 51, 50)')
                                )
                fig.layout.yaxis.color = 'white'
                fig.layout.legend.font.color = 'white'
                if CPU_CHART:
                    fig.add_trace(go.Scatter(x=chart_time_list, y=chart_cpu_list, name='СPU',
                                             line=dict(color="#2400FF")))
                if GPU_CHART:
                    fig.add_trace(go.Scatter(x=chart_time_list, y=chart_gpu_list, name='GPU',
                                             line=dict(color="#FF2026")))
                if RAM_CHART:
                    fig.add_trace(go.Scatter(x=chart_time_list, y=chart_ram_list, name='RAM',
                                             line=dict(color="#3CFF80")))
                if T_CPU_CHART:
                    fig.add_trace(go.Scatter(x=chart_time_list, y=chart_cpu_temperature_list, name='Temp_CPU',
                                             line=dict(color="#FFB800")))
                if T_GPU_CHART:
                    fig.add_trace(go.Scatter(x=chart_time_list, y=chart_gpu_temperature_list, name='Temp_GPU',
                                             line=dict(color="#AB00FF")))
                fig.update_layout(legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                    margin=dict(l=22, r=0, t=0, b=0))
                fig.write_image("data/fig.png", width=610, height=345)
                image = Image.open('data/fig.png').crop((0, 0, 610, 330))
                image.save('data/fig.png')
                image = pygame.image.load("data/fig.png")
                display.blit(image, (460, 10))
            print_text('C', 485, 13, font_size=30, font_color=(17, 255, 0) if CPU_CHART else (255, 36, 0))
            print_text('G', 505, 13, font_size=30, font_color=(17, 255, 0) if GPU_CHART else (255, 36, 0))
            print_text('R', 525, 13, font_size=30, font_color=(17, 255, 0) if RAM_CHART else (255, 36, 0))
            print_text('T', 545, 13, font_size=30, font_color=(17, 255, 0) if T_CPU_CHART else (255, 36, 0))
            print_text('cpu', 555, 23, font_size=15, font_color=(17, 255, 0) if T_CPU_CHART else (255, 36, 0))
            print_text('T', 580, 13, font_size=30, font_color=(17, 255, 0) if T_GPU_CHART else (255, 36, 0))
            print_text('gpu', 590, 23, font_size=15, font_color=(17, 255, 0) if T_GPU_CHART else (255, 36, 0))

            pygame.display.update()
            time_of_the_las_passage = datetime.datetime.now()
        for en in pygame.event.get():
            if en.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == '__main__':
    drawing()
