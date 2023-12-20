# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')




from flask import Flask
from app import create_app

app = create_app()

# 我們把原本的 @app.route() 分離出 2 個 Py 檔，一個是 __init__.py，建立 url 及 route 關聯。一個是 route.py 建立網頁的後端函數。

if __name__ == "__main__":
    app.run(debug=True, port=8000)