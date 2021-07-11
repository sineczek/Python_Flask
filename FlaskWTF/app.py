from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'co§n1eNaGiT4'



class Book:
    def __init__(self, title, amount, available):
        self.title = title
        self.amount = amount
        self.available = available


class BookForm(FlaskForm):

    def validate_amount_even(form, field):
        if field.data % 2 != 1:
            raise ValidationError('This number must be even!')


    title = StringField('Book title', validators=[DataRequired('Enter book title'),
                                                  Length(min=5,
                                                         max=50,
                                                         message="The title must have 5 - 50 characters")],
                        default='Unknown')
    amount = IntegerField('Amount', validators=[DataRequired('Enter amount'),
                          validate_amount_even],
                          default=1)
    available = BooleanField('Available')


@app.route('/', methods=['POST', 'GET'])
def index():
    book = Book(title='How to take a nice photo', amount=11, available=True)
    #form = BookForm(title='European Kings', amount=1, available=True)
    form = BookForm(obj=book)

    if form.validate_on_submit():

        form.populate_obj(book)
        return f'''<h1>Hello</h1>
                    <ul>
                        <li>{form.title.label}: {book.title}</li>
                        <li>{form.amount.label}: {book.amount}</li>
                        <li>{form.available.label}: {book.available}</li>
                    </ul>'''
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
