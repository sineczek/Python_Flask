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

#Lab2
@app.route('/cook/<string:receipt>/<int:step>')
def cook(receipt, step):
    print(request.query_string)
    print('----')
    print(request.args)
    font_size='100%'
    if 'font-size' in request.args:
        font_size = request.args['font-size']
    body = f'''<H1 style="font-size: { font_size }">In the receipt {receipt} you are on step {step}</H1>'''
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

"""
Zmienne środowiskowe

set FLASK_APP=nawa_pliku.py     # w terminalu ustawienie zmiennej środowiskowej dla flaska, defaultowo musi to być app.py
set FLSK_DEBUG=1                # zmienna która pozwala zmieniać zmiany w apce

"""
