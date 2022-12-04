#!/usr/bin/python3
"""
This file defines the state class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    States class: inherits from base links to MySQL table states
    """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
