#!/usr/bin/python3
""" Place Module for HBNB project """
from models import amenity
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
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
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if models.env_storage != 'db':
        @property
        def reviews(self):
            """ Getter attribute that returns the list of Review
                instances with place_id equals to current Place.id
            """
            list = []
            for i in models.storage.all(Review).values():
                if Review.place_id == self.id:
                    list.append(i)
            return list

        @property
        def amenities(self):
            """ Getter attribute that returns the list of Amenity intances
                based on the attribute amenity_ids that contains all
                Amenity.id linked to the Place
            """
            list = []
            for i in models.storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    list.append(i)
            return list

        @amenities.setter
        def amenities(self, obj=None):
            """Add an Amenity id to the list Amenity_ids"""
            if obj is not None and isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
