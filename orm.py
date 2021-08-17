import os
import json
from datetime import datetime
from sqlalchemy import (
    ForeignKey,
    desc,
    create_engine,
    func,
    Column,
    BigInteger,
    Integer,
    Float,
    String,
    Boolean,
    DateTime,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from pandas import read_csv

db = "postgresql://airbank:airbank123@192.168.31.16:5432/airbank"
engine = create_engine(db, echo=False)
Base = declarative_base()

# def json_object(_object):
#   data = dict(_object.__dict__)
#   data.pop('_sa_instance_state', None)
#   return data

# def json_child_list(data, name):
#   if name in data:
#     data[name] = [_object.json() for _object in data[name]]

# def json_child_object(data, name):
#   if name in data:
#     data[name] = data[name].json()

# class Game(Base):
#   __tablename__ = 'games'

#   Id = Column('id', Integer, primary_key=True)
#   UserId = Column('user_id', Integer, ForeignKey('users.id'))
#   Path = Column('path', String)
#   Icon = Column('icon', String)
#   Name = Column('name', String)
#   Github = Column('github', String)
#   Active = Column('active', Boolean)


#   def __init__(self, data):
#     self.UserId = data['user_id']
#     self.Icon = data['icon']
#     self.Name = data['name']
#     self.Github = data['github']
#     self.Active = False

#   def json(self):
#     data = json_object(self)
#     return data


class Operations:
    pass


class Transactions(Base):
    # Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'Transactions'
    __table_args__ = {'sqlite_autoincrement': True}
    # tell SQLAlchemy the name of column and its attributes:
    id = Column(Integer, primary_key=True, nullable=False)


Base.metadata.create_all(engine)
# Session = sessionmaker()
# Session.configure(bind=engine)
# session = Session()

if __name__ == "__main__":
    from pandas import to_datetime

    df = read_csv("/home/david/Downloads/Transactions.csv")
    df['createdAt'] = to_datetime(df['createdAt'])
    df['transactionDate'] = to_datetime(df['transactionDate'])
    df['updatedAt'] = to_datetime(df['updatedAt'])
    df.to_sql(
        con=engine,
        index_label='id',
        name=Transactions.__tablename__,
        if_exists='replace',
    )
