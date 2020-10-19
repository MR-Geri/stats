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
    ],
    [
        r'D:\PycharmProjects\stats\venv\Lib\site-packages\comtypes\\',
        r'D:\PycharmProjects\stats\dist\stats\comtypes'
    ],
    [
        r'D:\PycharmProjects\stats\venv\Lib\site-packages\pyttsx3\\',
        r'D:\PycharmProjects\stats\dist\stats\pyttsx3'
    ]
]


if __name__ == '__main__':
    for path in path_list:
        shutil.copytree(*path)
