import shutil

path_list = [
    [
        r'D:\PycharmProjects\stats\data\\',
        r'D:\PycharmProjects\stats\dist\stats\data'
    ],
    [
        r'D:\PycharmProjects\stats\venv\Lib\site-packages\\kaleido\\',
        r'D:\PycharmProjects\stats\\dist\stats\kaleido'
    ],
    [
        r'D:\PycharmProjects\stats\venv\Lib\site-packages\plotly\\',
        r'D:\PycharmProjects\stats\dist\stats\plotly'
    ]

]


if __name__ == '__main__':
    for path in path_list:
        shutil.copytree(*path)
