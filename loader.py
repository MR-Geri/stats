import shutil

path_list = [
    [
        r'C:\Users\ilyak\PycharmProjects\stats\data\\',
        r'C:\Users\ilyak\PycharmProjects\stats\dist\main\data'
    ],
    [
        r'C:\Users\ilyak\PycharmProjects\stats\venv\Lib\site-packages\\kaleido\\',
        r'C:\Users\ilyak\PycharmProjects\stats\\dist\main\kaleido'
    ],
    [
        r'C:\Users\ilyak\PycharmProjects\stats\venv\Lib\site-packages\plotly\\',
        r'C:\Users\ilyak\PycharmProjects\stats\dist\main\plotly'
    ]

]


if __name__ == '__main__':
    for path in path_list:
        shutil.copytree(*path)
