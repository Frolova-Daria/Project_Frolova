import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Street (SqlAlchemyBase):
    __tablename__ = 'B_Street'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    street = sqlalchemy.Column(sqlalchemy.String, nullable=True)




