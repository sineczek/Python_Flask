from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    # querry string - przekaywanie parametrów po ? i łączenie ich & np.: http://127.0.0.1:5000/?color=blue&style=italic
    # ?color=red&style=italic;">HACKED<h1 style="font-style:italic
    color = 'black'
    # print(request.query_string)
    if 'color' in request.args:
        color = request.args['color']
    style = 'normal'
    if 'style' in request.args:
        style = request.args['style']

    for p in request.args:
        print(p, request.args[p])
    time_now = datetime.now().strftime('%H:%M:%S')

    return f'<h1 style="color: {color};font-style:{style};">Flaskowe boje!</h1>\n' \
           '<h2>Jest teraz: {}</h2>' \
           '<h3><a href="/about">About</a></h3>' \
           '<h3><a href="/links">Links</a></h3>'.format(time_now)


@app.route("/about")
def about():
    a = 10
    b = 5
    return '<h1><a href="https://www.linkedin.com/in/michal-zaitz/">LinkedIn</a>\n {}</h1>' \
           '<h3><a href="/">Strona główna</a></h3>'.format(a / b)


# dynamiczny routing
@app.route('/cantor/<string:currency>/<int:amount>/')  # przekazywanie parametrów do "ruty"
def cantor(currency, amount):
    message = f'<h1>You selected {currency} and the amount {amount}</h1>'
    return message


"""# lab
@app.route("/cook/<string:co>/<int:kroki>")
def cook(co, kroki):
    body = f'<H1>In the receipt {co} you are on step {kroki}</H1>'
    return body"""


# Lab2
@app.route('/cook/<string:receipt>/<int:step>')
def cook(receipt, step):
    print(request.query_string)
    print('----')
    print(request.args)
    font_size = '100%'
    if 'font-size' in request.args:
        font_size = request.args['font-size']
    body = f'''<H1 style="font-size: {font_size}">In the receipt {receipt} you are on step {step}</H1>'''
    return body


@app.route('/links')
def links():
    body = '''<a href="http://www.google.com">Google</a> <br /> 
            <a href="http://www.bing.com">Bing!</a>
            <h3><a href="/">Strona główna</a></h3>'''
    return body


"""    return '<h1>Linki do wyszukiwarek: </h1>' \
           '<h3><a href="http://www.google.com">Google</a></h3>' \
           '<h3><a href="http://www.bing.com">Bing!</a></h3>' \
           '<h3><a href="/">Strona główna</a></h3>'"""
# bez tego naley używać "flusk run"
if __name__ == '__main__':
    app.run()


# formularz
@app.route('/exchange')
def excgange():
    body = '''
        <form id="exchange_form" action="/exchange_process" method="POST">
            <label for="currency">Currency</label>
            <input type="text" id="currency" name="currency" value="EUR"><br>
            <label for="amount">Amount</label>
            <input type="text" id="amount" name="amount" value="100"><br>
            <input type="submit" value="Send">
        </form>
    '''
    return body


@app.route('/exchange_process', methods=['POST'])
def exchange_process():
    currency = 'EUR'
    if 'currency' in request.form:
        currency = request.form['currency']

    amount = '100'
    if 'amount' in request.form:
        amount = request.form['amount']

    body = f'You want to exchange {amount} {currency}'

    return body

#formularz LAB
@app.route('/ocen_ciacho')
def ocen_ciacho():
    body = ''' 
        <form id="rating" action="/zapisana_ocena" method="POST"> 
        <label for=note>What is your note for the receipt?</label><br> 
        <select id="nore" name="note"> 
        <option value="5">It is great!</option> 
        <option value="4">It is very good</option> 
        <option value="3" selected>It is just good</option> 
        <option value="2">It was poor</option> 
        <option value="1">It was horrible!</option> </select><br> 
        <label for=comment>Write down your comments:</label><br> 
        <textarea id="comment" name="comment" rows="3" cols="50"> </textarea><br> 
        <label for="decision">Would you cook it for your family?</label><br> 
        <input type="checkbox" id="decision" name="decision"><br> 
        <input type="submit" value="Share my feedback"> </form> '''
    return body

@app.route('/zapisana_ocena', methods=['POST'])
def zapisana_ocena():

    note = 3
    if 'note' in request.form:
        note = request.form['note']

    comment=''
    if 'comment' in request.form:
        comment = request.form['comment']


    decision = False
    if 'decision' in request.form:
        decision = True

    message = f'''
        Your rating was: {note}<br>
        Your comment was: {comment}<br> 
        Your decision was {decision} '''
    return message

"""
Zmienne środowiskowe

set FLASK_APP=nawa_pliku.py     # w terminalu ustawienie zmiennej środowiskowej dla flaska, defaultowo musi to być app.py
set FLSK_DEBUG=1                # zmienna która pozwala zmieniać zmiany w apce

"""
