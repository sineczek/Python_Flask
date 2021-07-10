from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'co§n1eNaGiT4'


class BookForm(FlaskForm):

    def validate_amount_even(form, field):
        if field.data % 2 != 1:
            raise ValidationError('This number must be even!')


    title = StringField('Book title', validators=[DataRequired('Enter book title'),
                                                  Length(min=5,
                                                         max=50,
                                                         message="The title must have 5 - 50 characters")])
    amount = IntegerField('Amount', validators=[DataRequired('Enter amount'),
                          validate_amount_even])
    available = BooleanField('Available')


@app.route('/', methods=['POST', 'GET'])
def index():

    form = BookForm(csrf_enabled=True)
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
