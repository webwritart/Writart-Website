import datetime
from flask_sqlalchemy import table
from extensions import db


def calculate_age(birthdate):
    year, month, day = map(int, birthdate.split("-"))
    today = datetime.date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age


def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


# tables_dict = {table.__tablename__: table for table in db.Model.__class__()}


# def table_object(table_name):
#     return tables_dict.get(table_name)
