import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Seller (SqlAlchemyBase):
    __tablename__ = 'B_Seller'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    fio = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    pasport_series = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    pasport_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)




