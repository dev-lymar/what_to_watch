import csv

import click

from . import app, db
from .models import Opinion


@app.cli.command('load_opinions')
def load_opinions():
    """Uploading opinions to the database."""
    with open('opinions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            opinion = Opinion(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    click.echo(f'Loaded {counter} opinions')