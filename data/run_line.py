import requests
from bs4 import BeautifulSoup


def run_line():
    running_line = ['' for _ in range(2)]
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/85.0.4183.102 YaBrowser/20.9.2.102 Yowser/2.5 Safari/537.36',
               'accept': '*/*'}
    data_soup = []
    for url in ['usd', 'eur']:
        soup = BeautifulSoup(requests.get(f'https://mainfin.ru/currency/{url}/lipeck',
                                          headers=headers).text,
                             'html.parser')
        for i in soup.find_all('td', class_='mark-text'):
            data_soup.append(f'{float(i.get_text()):.2f}')
    try:
        text = ' ' * (7 - len(data_soup[0]) - len(data_soup[1])) + f'$ = {data_soup[0]}  € = {data_soup[1]}'
    except:
        text = ''
    running_line[1] = [[[(text, 60, 140)], (255, 255, 255)]]
    soup = BeautifulSoup(requests.get('https://world-weather.ru/pogoda/russia/lipetsk/', headers=headers).text,
                         'html.parser')
    # Ощущается как °C
    # Вероятность осадков %
    # Давление мм рт. ст.
    # Скорость ветра м/с
    # Влажность воздуха
    items = soup.find_all('div', class_='pane')
    data = [[['' for _ in range(5)], ()] for _ in range(4)]
    col = [(35, 255, 0), (0, 0, 255), (255, 255, 0), (128, 0, 255)]
    data_find = ['weather-feeling', 'weather-probability', 'weather-pressure', 'weather-wind', 'weather-humidity']
    for i in range(4):
        for f in data_find:
            s = ''
            for te in items[i].find_all('td', class_=f):
                s += te.get_text(strip=True) + ' '
            data[i][0][data_find.index(f)] = (s.rstrip(), 67 + 8 * (19 - len(s.rstrip())), 140)
        data[i][1] = col[i]
    running_line[0] = data
    return running_line
