from flask import Flask, render_template, url_for, request, flash, g
from datetime import datetime
import sqlite3

# konfiguracja sqlite3
app_info = {'db_file': '/Users/sinq/nauka/Python_Flask/NicerApp/data/cantor.db'}

app = Flask(__name__)

app.config['SECRET_KEY'] = 'CosTajnegoNaGitHubaNiePrzewidzianego'


def get_db():
    if not hasattr(g, 'sqlite_db'):
        conn = sqlite3.connect(app_info['db_file'])
        conn.row_factory = sqlite3.Row
        g.sqlite_db = conn
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite3_db'):
        g.sqlite_db.close()


class Currency:

    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self):
        return '<Currency {}>'.format(self.code)


class CantorOffer:

    def __init__(self):
        self.currencies = []
        self.denied_codes = []

    def load_offer(self):
        self.currencies.append(Currency('USD', 'Dollar', 'united-states.png'))
        self.currencies.append(Currency('EUR', 'Euro', 'european-union.png'))
        self.currencies.append(Currency('JPY', 'Yen', 'japan.png'))
        self.currencies.append(Currency('GBP', 'Pound', 'united-kingdom.png'))
        self.currencies.append(Currency('PLN', 'Polski Złoty', 'poland.png'))
        self.denied_codes.append('USD')

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency
        return Currency('unknown', 'unknown', 'pirate-flag.png')


class PriorityType:
    def __init__(self, code, description, selected):
        self.code = code
        self.description = description
        self.selected = selected


class NotificationPriorities:
    def __init__(self):
        self.list_of_priorities = []

    def load_priorities(self):
        self.list_of_priorities.append(PriorityType('high', 'HIGH PRIORITY', False))
        self.list_of_priorities.append(PriorityType('medium', 'MEDIUM', False))
        self.list_of_priorities.append(PriorityType('normal', 'NOT URGENT', True))
        self.list_of_priorities.append(PriorityType('low', 'REMARK', False))

    def get_priority_by_code(self, code):
        for p in self.list_of_priorities:
            if p.code == code:
                return p
        return PriorityType('normal', 'NOT URGENT', True)


@app.route('/')
def index():
    return render_template('index.html', active_menu='home')


@app.route('/exchange', methods=['POST', 'GET'])
def exchange():
    offer = CantorOffer()
    offer.load_offer()
    if request.method == 'GET':
        return render_template('exchange.html', active_menu='exchange', offer=offer)

    else:
        print("Debug: starting exchange in POST mode")
        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']
        amount = 100
        if 'amount' in request.form:
            amount = request.form['amount']

        if currency in offer.denied_codes:
            flash('The currency {} cannot be accepted'.format(currency))
        elif offer.get_by_code('unknown') == 'unknown':
            flash('The selected currency is unknown and cannot be accepted')
        else:
            db = get_db()
            sql_command = 'insert into transactions(currency, amount, user) values(?, ?, ?)'
            db.execute(sql_command, [currency, amount, 'admin'])
            db.commit()
            flash('Requested to exchange {} was accepted'.format(currency))

        return render_template('exchange_result.html', active_menu='exchange', currency=currency,
                               amount=amount, currency_info=offer.get_by_code(currency))


@app.route('/hotel_form', methods=['GET', 'POST'])
def hotel_form():
    notification_priorities = NotificationPriorities()
    notification_priorities.load_priorities()

    if request.method == 'GET':
        return render_template('my_form.html', active_menu='hotel_form',
                               list_of_priorities=notification_priorities.list_of_priorities)

    else:
        room_number = request.form['room_number'] if 'room_number' in request.form else ''
        guest_name = request.form['guest_name'] if 'guest_name' in request.form else ''
        notification_text = request.form['notification_text'] if 'notification_text' in request.form else ''
        priority = request.form['priority'] if 'priority' in request.form else 'normal'

        priority_type = notification_priorities.get_priority_by_code(priority)
        print('found', priority_type.code)

        flash('Notification has been sent')

        the_hour = datetime.now().hour
        raise_priority = (the_hour >= 19 or the_hour < 6) and priority == 'medium'

        if raise_priority:
            priority = 'high'
            flash('Rising priority from medium to high')

        return render_template('complain.html', active_menu='hotel_menu',
                               room_number=room_number, guest_name=guest_name,
                               notification_text=notification_text, priority_type=priority_type)


@app.route('/history')
def history():
    db = get_db()
    sql_command = 'select id, currency, amount, trans_date from transactions;'
    cur = db.execute(sql_command)  # kursor wykonujący polecenie i przechowujący w zmiennejk
    transactions = cur.fetchall()  # pobieranie wszystkich danych z zapytania

    return render_template('history.html', active_menu='history', transactions=transactions)


if __name__ == '__main__':
    app.run()
