#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
import models
from sqlalchemy import Column, String
from sqlalchemy import.orm relationship


class Amenity(BaseModel, Base):
    """Amenity to have"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
