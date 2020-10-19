import os
import clr
import psutil
import datetime


dll_file_name = os.path.abspath(os.path.dirname(__file__)) + R'\OpenHardwareMonitorLib.dll'
clr.AddReference(dll_file_name)
from OpenHardwareMonitor import Hardware

handle = Hardware.Computer()
handle.MainboardEnabled = handle.CPUEnabled = handle.GPUEnabled = handle.HDDEnabled = True
handle.Open()


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


def temperatures():
    """ Считывание температуры с датчиков. """
    v_tem_1 = ['SYS', 'PCH', 'CPU_GP', 'PCI_E', 'VRM', 'AUX']
    v_tem_2 = ['GPU', 'HDD 1', 'HDD 2']
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


temperature = {}
inf = {"CPU": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       "RAM": [16329, 0, 0, 0],
       "Диск C": [90.4, 0, 0, 0],
       "Диск D": [374.81, 0, 0, 0],
       "Диск G": [250.34, 0, 0, 0],
       "Диск F": [430.52, 0, 0, 0],
       "Диск H": [250.65, 0, 0, 0],
       "Диск E": [931.51, 0, 0, 0],
       "time": [12, 11, 57, 00]}
