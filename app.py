from flask import Flask, render_template, request
from ResultOnto import get_result


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('Input_1.html')


@app.route('/submit/', methods=['POST'])
def submit():
    data = request.form
    result = get_result(data['city'])
    result['base_url'] = request.base_url.replace('/submit/', '')
    result['city'] = data['city'].upper()
    return render_template('result.html', result=result)


@app.route('/open/<city>', methods=['GET'])
def open(city):
    # data = request.form
    result = get_result(city)
    result['base_url'] = request.base_url.replace(request.base_url, 'http://127.0.0.1:5000')
    result['city'] = city.upper()
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)


