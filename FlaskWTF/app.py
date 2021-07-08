from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'co§n1eNaGiT4'


class BookForm(FlaskForm):

    title = StringField('Book title')
    amount = IntegerField('Amount')
    available = BooleanField('Available')


@app.route('/', methods=['POST', 'GET'])
def index():
    form = BookForm()

    if form.validate_on_submit():
        return f'''<h1>Hello</h1>
                    <ul>
                        <li>{form.title.label}: {form.title.data}</li>
                        <li>{form.amount.label}: {form.amount.data}</li>
                        <li>{form.available.label}: {form.available.data}</li>
                    </ul>'''
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
