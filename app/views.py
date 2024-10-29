from random import randrange

from flask import redirect, render_template, url_for, flash, abort

from app.services import random_opinion

from . import app, db
from .forms import OpinionForm
from .models import Opinion


@app.route('/')
def index_view():
    opinion = random_opinion()

    if opinion is not None:
            return render_template('opinion.html', opinion=opinion)

    abort(404)




@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    form = OpinionForm()

    if form.validate_on_submit():
        text = form.text.data
        if Opinion.query.filter_by(text=text).first() is not None:
            flash('This opinion has been left before!')
            return render_template('add_opinion.html', form=form)

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
