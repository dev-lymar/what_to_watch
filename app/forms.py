from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


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
