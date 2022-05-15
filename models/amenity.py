#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
import models
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity to have"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
