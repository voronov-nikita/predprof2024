from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/vvod', methods=['GET', 'POST'])
def vvod():
    if request.method == 'POST':
        data = request.form['data']
        print(data)
    return render_template('vvod.html')

@app.route('/list')
def list():
    return render_template('list.html')


if __name__ == '__main__':
    app.run(debug=True)
