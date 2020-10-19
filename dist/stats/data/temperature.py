import os
import clr


dll_file_name = os.path.abspath(os.path.dirname(__file__)) + R'\OpenHardwareMonitorLib.dll'
clr.AddReference(dll_file_name)
from OpenHardwareMonitor import Hardware

handle = Hardware.Computer()
handle.MainboardEnabled = handle.CPUEnabled = handle.GPUEnabled = handle.HDDEnabled = True
handle.Open()


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
