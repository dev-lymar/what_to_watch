from datetime import datetime
from random import randrange
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'

db = SQLAlchemy(app)


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    source = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now())


class OpinionForm(FlaskForm):
    title = StringField(
        'Enter the title of the film',
        validators=[DataRequired(message='Required field'),
                    Length(1, 128)]
        )
    text = TextAreaField(
        'Write an opinion',
        validators=[DataRequired(message='Required field')]
    )
    source = URLField(
        'Add a link to an in-depth review of the film',
        validators=[Length(1, 256), Optional()])
    submit = SubmitField('Add opinion')


@app.route('/')
def index_view():
    quantity = Opinion.query.count()

    if not quantity:
        return 'No opinions in database'

    offset_value = randrange(quantity)
    opinion = Opinion.query.offset(offset_value).first()
    return render_template('opinion.html', opinion=opinion)


@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    form = OpinionForm()

    if form.validate_on_submit():
        opinion = Opinion(
            title=form.title.data,
            text=form.text.data,
            source=form.source.data
        )

        db.session.add(opinion)
        db.session.commit()

        return redirect(url_for('opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)

@app.route('/opinions/<int:id>')
def opinion_view(id):
    opinion = Opinion.query.get_or_404(id)
    return render_template('opinion.html', opinion=opinion)


if __name__ == '__main__':
    app.run()
