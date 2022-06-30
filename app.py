# print("ddd")
from flask import Flask
import pandas
import openpyxl

app = Flask(__name__)

@app.route("/")
def hello_world():
    df = pandas.read_excel("1.xlsx", sheet_name="l1")

    # print whole sheet data
    # print(df)
    l1 = []
    l1 = df.values.tolist()
    str1=""
    for item in l1:
        str1+=str(item[0]) + " козел "
    return str1

@app.route("/api/ezh/<int:id>")
def ezh_func(id):
    return "Сергей не съел " + str(id) + " ёжиков"

if __name__ == '__main__':
    app.run()


