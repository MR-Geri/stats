import requests
from bs4 import BeautifulSoup


def run_line():
    running_line = ['' for _ in range(2)]
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/84.0.4147.86 YaBrowser/20.8.0.894 Yowser/2.5 Yptp/1.23 Safari/537.36',
               'accept': '*/*'}
    data_soup = []
    for url in ['евро', 'доллар']:
        soup = BeautifulSoup(requests.get(f'https://yandex.ru/search/?text=курс%20{url}&lr=9&clid=2270455&win=431'
                                          f'&suggest%27%20f%27_reqid=884927702159387871037738163558535&src=suggest_Rec',
                                          headers=headers).text,
                             'html.parser')
        for i in soup.find_all('input', class_='input__control'):
            data_soup.append(i.get('value').split()[-1])
    try:
        text = ' ' * (7 - len(str(data_soup[5])) - len(str(data_soup[2]))) + f'$ = {data_soup[5]}  € = {data_soup[2]}'
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
