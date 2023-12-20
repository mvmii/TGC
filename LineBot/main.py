# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# Flask + ECharts 資料視覺化
# 教學出處網址
# https://medium.com/%E5%B7%A5%E7%A8%8B%E9%9A%A8%E5%AF%AB%E7%AD%86%E8%A8%98/flask-echarts-%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96-52e0784e1b7d

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    data=[{'name': 'rose 1', 'value': 40},
        {'name': 'rose 2', 'value': 38},
        {'name': 'rose 3', 'value': 32},
        {'name': 'rose 4', 'value': 30},
        {'name': 'rose 5', 'value': 28},
        {'name': 'rose 6', 'value': 26},
        {'name': 'rose 7', 'value': 22},
        {'name': 'rose 8', 'value': 18}]
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)