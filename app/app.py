import sys
sys.path.append("../")

from flask import Flask, render_template, request
from src.database import *


app = Flask(__name__)


createDatabase()


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(getAallData())
        date = request.form['date']
        # datas = getAallData()[int(date)]
        # print(datas)
        render_template('index.html', dateee=date)

    return render_template('index.html')


@app.route('/vvod', methods=['GET', 'POST'])
def vvod():
    if request.method == 'POST':
        date = request.form['date']
        # number = request.form['number']
        # window = request.form['window']
        # light = request.form['light']

        # if date and number and window and light:
        addDataDate(date, "")
        addDataFloors("0", "")
        addDataWindows("1", "")
        addDataRooms("2", "")
    return render_template('vvod.html')


@app.route('/list')
def list():
    return render_template('list.html')


if __name__ == '__main__':
    app.run(debug=True)
