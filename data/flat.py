import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Flat (SqlAlchemyBase):
    __tablename__ = 'flat'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    street = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    house = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    flat = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    area = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    seller = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    sale = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    kol = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)


