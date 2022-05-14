#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
import models


class State(BaseModel, Base):
    """ State class """
    if models.env_storage == 'bd':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes State. """
        super().__init__(*args, **kwargs)

    if models.env_storage != 'bd':
        @property
        def cities(self):
            """getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            id_list = []
            for i in storage.all(City).values():
                if City.state_id == self.id:
                    id_list.append(i)
            return id_list
