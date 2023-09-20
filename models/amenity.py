#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents a class Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table amenities.

    Attributes:
        __tablename__ (Str): The name of the MySQL table to store Amenities.
        name(Str): The amenity name.
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
