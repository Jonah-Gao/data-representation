from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# init
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///unicode_table.sqlite3'  # db location

db = SQLAlchemy(app)

# database structure
class Unicode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char = db.Column(db.String(1), unique=True)
    unicode = db.Column(db.String(6), unique=True)


with app.app_context():
    db.create_all()  # creates database

    for i in range(128):  # adds unicode characters into database
        new_unicode = Unicode(char=chr(i), unicode=f"U+{str(hex(i)).split('x')[-1].zfill(4).upper()}")
        db.session.add(new_unicode)
        db.session.commit()

# takes a long time to add all the unicode characters, therefore only adding the ascii characters

with app.app_context():
    unicode = Unicode.query.filter_by(char='A').first()  # filter by char
    print(unicode.unicode)
    char = Unicode.query.filter_by(unicode='U+0041').first()  # filter by unicode
    print(char.char)
