# initdb.py

import os

from .db import get_db

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def initdb():
    db = get_db()
    with open(os.path.join(__location__, 'initdb.sql')) as f:
        with db.cursor() as c:
            c.execute(f.read())
    db.commit()
