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


@app.route('/hotel_form', methods=['GET', 'POST'])
def hotel_form():
    if request.method == 'GET':
        return render_template('my_form.html')

    else:
        room_number = request.form['room_number']
        """if room_number in request.form:
            room_number = request.form['room_number']"""

        guest_name = request.form['guest_name']
        """if guest_name in request.form:
            guest_name = request.form['guest_name']"""

        complain = request.form['complain']
        """if complain in request.form:
            complain = request.form['complain']"""

        return render_template('complain.html', room_number=room_number, guest_name=guest_name, complain=complain)

