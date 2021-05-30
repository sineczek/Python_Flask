from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is index'


@app.route('/exchange', methods=['POST', 'GET'])
def exchange():
    if request.method == 'GET':
        return render_template('exchange.html')

    else:
        currency = 'EUR'
        if currency in request.form:
            currency = request.form['currency']

        amount = '100'
        if amount in request.form:
            amount = request.form['amount']

        return render_template('exchange_result.html', currency=currency, amount=amount)