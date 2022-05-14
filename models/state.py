#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Foreignkey
from os import getenv
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City
        instances with state_id equals to the current State.id"""
        id_list = []
        for i in storage.all(City).values():
            if state_id == self.id:
                id_list.append(i)
        return id_list
