#!/usr/bin/python3
""" Place Module for HBNB project """
from statistics import mode
from models import amenity
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity

if models.env_storage == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    if models.env_storage == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
        amenities = relationship("Amenity", secundary=place_amenity,
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """"""
            list = []
            for i in models.storage.all(Review).values():
                if Review.place_id == self.id:
                    list.append(i)
            return list

        @property
        def amenities(self):
            """"""
            list = []
            for i in models.storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    list.append(i)
            return list

        """ @amenities.setter
        def amenities(self, obj=None):
            """"""
            if obj is not None and isinstance(obj, Amenity): """
