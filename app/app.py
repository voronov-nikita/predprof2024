import sys
sys.path.append("../")

from src.database import *

from flask import Flask, render_template,request

app = Flask(__name__)


createDatabase()

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        datas = getAallData()
        render_template('index.html', answer="Данные получены корректно", numbers=datas[3], count_room=datas[1], newdata=datas)
    
    return render_template('index.html')

@app.route('/vvod', methods=['GET', 'POST'])
def vvod():
    if request.method == 'POST':
        date = request.form['date']
        number = request.form['number']
        window = request.form['window']
        light = request.form['light']
        
        print(date, number, window, light)
        
        if date and number and window and light:
            addDataDate(date, "")
            addDataFloors(number, "")
            addDataWindows(window, "")
            addDataRooms(light, "")
        else:
            print("Не довведенны необходимые данные")
    return render_template('vvod.html')

@app.route('/list')
def list():
    return render_template('list.html')


if __name__ == '__main__':
    app.run(debug=True)
