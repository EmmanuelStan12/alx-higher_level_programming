#!/usr/bin/python3
"""
This file defines the state class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class: inherits from base links to MySQL table states
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
