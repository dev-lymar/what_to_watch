from random import randrange
from app.models import Opinion


def random_opinion():
    quantity = Opinion.query.count()
    offset_value = randrange(quantity)
    opinion = Opinion.query.offset(offset_value).first()
    return opinion
