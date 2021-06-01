from flask import Flask, render_template, url_for, request

app = Flask(__name__)


# przechowywanie zmiennych walut
class Currency:

    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self):  # textowa reprezentacja wartości z class'y
        return '<Currency {}>'.format(self.code)


class CantorOffer:

    def __init__(self):
        self.currencies = []

    def load_offer(self):
        self.currencies.append(Currency('USD', 'Dollar', 'united-states.png'))
        self.currencies.append(Currency('EUR', 'Euro', 'european-union.png'))
        self.currencies.append(Currency('JPY', 'Yen', 'japan.png'))
        self.currencies.append(Currency('GBP', 'Pound', 'united-kingdom.png'))
        self.currencies.append(Currency('PLN', 'Polski Złoty', 'poland.png'))

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
    return 'This is index'


@app.route('/exchange', methods=['POST', 'GET'])
def exchange():
    offer = CantorOffer()
    offer.load_offer()
    if request.method == 'GET':
        return render_template('exchange.html', offer=offer)

    else:
        currency = 'EUR'  # request.form['currency']
        if 'currency' in request.form:
            currency = request.form['currency']

        amount = 100  # request.form['amount']
        if 'amount' in request.form:
            amount = request.form['amount']

        return render_template('exchange_result.html', currency=currency,
                               amount=amount, currency_info=offer.get_by_code(currency))


@app.route('/hotel_form', methods=['GET', 'POST'])
def hotel_form():
    notification_priorities = NotificationPriorities()
    notification_priorities.load_priorities()

    if request.method == 'GET':
        return render_template('my_form.html', list_of_priorities=notification_priorities.list_of_priorities)

    else:
        room_number = request.form['room_number'] if 'room_number' in request.form else ''
        guest_name = request.form['guest_name'] if 'guest_name' in request.form else ''
        notification_text = request.form['notification_text'] if 'notification_text' in request.form else ''
        priority = request.form['priority'] if 'priority' in request.form else 'normal'

        priority_type = notification_priorities.get_priority_by_code(priority)
        print('found', priority_type.code)
        return render_template('complain.html',
                               room_number=room_number, guest_name=guest_name,
                               notification_text=notification_text, priority_type=priority_type)


"""          CIACH

        room_number = 'None'  # request.form['room_number']
        if 'room_number' in request.form:
            room_number = request.form['room_number']

        guest_name = 'None'  # request.form['guest_name']
        if 'guest_name' in request.form:
            guest_name = request.form['guest_name']

        complain = 'None'  # request.form['complain']
        if 'complain' in request.form:
            complain = request.form['complain']
        priority = request.form['priority']
        if priority == 'High':
            priority == 'Critical notification content'
        elif priority == 'Medium':
            priority == 'Important notification content'
        else:
            priority == 'Notification content'
        return render_template('complain.html', room_number=room_number, guest_name=guest_name, complain=complain,
                               priority=priority)
                               
                               
              CIACH                 """
