import datetime
import plotly.graph_objs as go
import pygame
from PIL import Image
import GPUtil


chart_time_list = [i for i in range(1, 61)]
chart_cpu_list = []
chart_gpu_list = []
chart_ram_list = []
chart_cpu_temperature_list = []
chart_gpu_temperature_list = []


def load_colors(stats):
    if stats < 25:
        return 34, 139, 34
    elif stats < 50:
        return 102, 0, 255
    elif stats < 75:
        return 102, 102, 0
    return 255, 36, 0


def print_text(display, message, x, y, font_color=(255, 255, 255), font_size=30, font_type='data/shrift.otf'):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


def blit_all_rect(display, APP):
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


def draw_disk(display, inf):
    # Блок инфы дисков Правый
    pygame.draw.rect(display, (54, 35, 8), (785, 25, 270, 90))
    pygame.draw.rect(display, (102, 102, 0), (785, 25, int(270 / 100 * int(inf['Диск D'][3])), 90))
    #
    print_text(display, 'D: ' + str(inf['Диск D'][0]) + '/GB/', 790, 27, font_size=28)
    print_text(display, 'USE: ' + str(inf['Диск D'][1]) + '/GB/', 790, 57, font_size=28)
    print_text(display, 'FREE: ' + str(inf['Диск D'][2]) + '/GB/', 790, 87, font_size=28)
    print_text(display, str(inf['Диск D'][3]) + '%', 1000, 27, font_size=28)

    # Обновляется
    pygame.draw.rect(display, (54, 35, 8), (785, 130, 270, 90))
    pygame.draw.rect(display, (102, 102, 0), (785, 130, int(270 / 100 * int(inf['Диск F'][3])), 90))
    #
    print_text(display, 'F: ' + str(inf['Диск F'][0]) + '/GB/', 790, 132, font_size=28)
    print_text(display, 'USE: ' + str(inf['Диск F'][1]) + '/GB/', 790, 162, font_size=28)
    print_text(display, 'FREE: ' + str(inf['Диск F'][2]) + '/GB/', 790, 192, font_size=28)
    print_text(display, str(inf['Диск F'][3]) + '%', 1000, 132, font_size=28)
    # Обновляется
    pygame.draw.rect(display, (54, 35, 8), (785, 235, 270, 90))
    pygame.draw.rect(display, (102, 102, 0), (785, 235, int(270 / 100 * int(inf['Диск E'][3])), 90))
    #
    print_text(display, 'E: ' + str(inf['Диск E'][0]) + '/GB/', 790, 237, font_size=28)
    print_text(display, 'USE: ' + str(inf['Диск E'][1]) + '/GB/', 790, 267, font_size=28)
    print_text(display, 'FREE: ' + str(inf['Диск E'][2]) + '/GB/', 790, 297, font_size=28)
    print_text(display, str(inf['Диск E'][3]) + '%', 1000, 237, font_size=28)
    # Обновляется
    pygame.draw.rect(display, (54, 35, 8), (475, 25, 270, 90))
    pygame.draw.rect(display, (102, 102, 0), (475, 25, int(270 / 100 * int(inf['Диск C'][3])), 90))
    #
    print_text(display, 'C: ' + str(inf['Диск C'][0]) + '/GB/', 480, 27, font_size=28)
    print_text(display, 'USE: ' + str(inf['Диск C'][1]) + '/GB/', 480, 57, font_size=28)
    print_text(display, 'FREE: ' + str(inf['Диск C'][2]) + '/GB/', 480, 87, font_size=28)
    print_text(display, str(inf['Диск C'][3]) + '%', 690, 27, font_size=28)
    # Обновляется
    pygame.draw.rect(display, (54, 35, 8), (475, 130, 270, 90))
    pygame.draw.rect(display, (102, 102, 0), (475, 130, int(270 / 100 * int(inf['Диск G'][3])), 90))
    #
    print_text(display, 'G: ' + str(inf['Диск G'][0]) + '/GB/', 480, 132, font_size=28)
    print_text(display, 'USE: ' + str(inf['Диск G'][1]) + '/GB/', 480, 162, font_size=28)
    print_text(display, 'FREE: ' + str(inf['Диск G'][2]) + '/GB/', 480, 192, font_size=28)
    print_text(display, str(inf['Диск G'][3]) + '%', 690, 132, font_size=28)
    # Обновляется
    pygame.draw.rect(display, (54, 35, 8), (475, 235, 270, 90))
    pygame.draw.rect(display, (102, 102, 0), (475, 235, int(270 / 100 * int(inf['Диск H'][3])), 90))
    #
    print_text(display, 'H: ' + str(inf['Диск H'][0]) + '/GB/', 480, 237, font_size=28)
    print_text(display, 'USE: ' + str(inf['Диск H'][1]) + '/GB/', 480, 267, font_size=28)
    print_text(display, 'FREE: ' + str(inf['Диск H'][2]) + '/GB/', 480, 297, font_size=28)
    print_text(display, str(inf['Диск H'][3]) + '%', 690, 237, font_size=28)


def draw_time(display, inf):
    pygame.draw.rect(display, (50, 51, 50), (770, 350, 300, 120))
    print_text(display, f'{datetime.datetime.now().strftime("%H:%M")}', 782, 350, font_size=100)
    print_text(display, f'{datetime.datetime.now().strftime("%d-%m-%Y")}', 790, 440)
    time_out = str(inf['time'][1] + inf['time'][0] * 24) + ':' + str(inf['time'][2]) + ':' + str(inf['time'][3])
    print_text(display, ' ' * (8 - len(time_out)) + time_out, 965, 445, font_size=22)


def draw_statistic(display, inf, temp, cpu_chart, gpu_chart, ram_chart, t_cpu_chart, t_gpu_chart):
    global chart_time_list, chart_cpu_list, chart_gpu_list, \
        chart_ram_list, chart_cpu_temperature_list, chart_gpu_temperature_list
    print_text(display, f'AUX-{temp["AUX"]} CGP-{temp["CPU_GP"]} SYS-{temp["SYS"]}',
               58, 40, font_size=30)
    print_text(display, f'PCH-{temp["PCH"]} PCI-{temp["PCI_E"]} VRM-{temp["VRM"]}',
               58, 75, font_size=30)
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
    print_text(display, 'CPU-' + cp + ' (' + f"{cpu}%) Core-" + str(temp['CPU'][-1]), 32, 58 + 40 * 3, font_size=30)
    print_text(display, 'GPU-' + str(temp['GPU']) + ' (' + f"{gpu}%) " + f"{int(gp.memoryFree)}MB",
               32, 58 + 40 * 4, font_size=30)
    print_text(display, 'RAM-' + str(inf['RAM'][0]) + 'MB        ' + str(inf['RAM'][2]) + '%',
               32, 58 + 40 * 5, font_size=30)
    print_text(display, 'use-' + str(inf['RAM'][3]) + 'MB free-' + str(inf['RAM'][1]) + 'MB',
               33, 58 + 40 * 6, font_size=30)
    if cpu_chart or gpu_chart or ram_chart or t_cpu_chart or t_gpu_chart:
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
        if cpu_chart:
            fig.add_trace(go.Scatter(x=chart_time_list, y=chart_cpu_list, name='СPU',
                                     line=dict(color="#2400FF")))
        if gpu_chart:
            fig.add_trace(go.Scatter(x=chart_time_list, y=chart_gpu_list, name='GPU',
                                     line=dict(color="#FF2026")))
        if ram_chart:
            fig.add_trace(go.Scatter(x=chart_time_list, y=chart_ram_list, name='RAM',
                                     line=dict(color="#3CFF80")))
        if t_cpu_chart:
            fig.add_trace(go.Scatter(x=chart_time_list, y=chart_cpu_temperature_list, name='Temp_CPU',
                                     line=dict(color="#FFB800")))
        if t_gpu_chart:
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
        print_text(display, 'all', 480, 15, font_size=12, font_color=(255, 255, 255))
        print_text(display, 'off', 480, 26, font_size=12, font_color=(255, 255, 255))
        print_text(display, 'C', 504, 13, font_size=30, font_color=(17, 255, 0) if cpu_chart else (255, 36, 0))
        print_text(display, 'G', 524, 13, font_size=30, font_color=(17, 255, 0) if gpu_chart else (255, 36, 0))
        print_text(display, 'R', 544, 13, font_size=30, font_color=(17, 255, 0) if ram_chart else (255, 36, 0))
        print_text(display, 'T', 564, 13, font_size=30, font_color=(17, 255, 0) if t_cpu_chart else (255, 36, 0))
        print_text(display, 'cpu', 574, 23, font_size=15, font_color=(17, 255, 0) if t_cpu_chart else (255, 36, 0))
        print_text(display, 'T', 599, 13, font_size=30, font_color=(17, 255, 0) if t_gpu_chart else (255, 36, 0))
        print_text(display, 'gpu', 609, 23, font_size=15, font_color=(17, 255, 0) if t_gpu_chart else (255, 36, 0))
