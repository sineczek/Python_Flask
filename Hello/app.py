from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    time_now = datetime.now().strftime('%H:%M:%S')
    return '<h1>Flaskowe boje!</h1>\n' \
           '<h2>Jest teraz: {}</h2>' \
           '<h3><a href="/about">About</a></h3>' \
           '<h3><a href="/links">Links</a></h3>'.format(time_now)

@app.route("/about")
def about():
    a = 10
    b = 5
    return '<h1><a href="https://www.linkedin.com/in/michal-zaitz/">LinkedIn</a>\n {}</h1>' \
           '<h3><a href="/">Strona główna</a></h3>'.format(a / b)

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

set FLASK_APP=nawa_pliku.py     #w terminalu ustawienie zmiennej środowiskowej dla flaska, defaultowo musi to być app.py
set FLSK_DEBUG=1                #zmienna która pozwala zmieniać zmiany w apce

"""
