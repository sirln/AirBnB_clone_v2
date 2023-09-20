#!/usr/bin/python3
""" Place Module for HBNB project """
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ The class Place representation of MySql Database.

    Inherits from SQLAlchemy Base and links to the MySql table Place.

    Attributes:
    __tablename__(str): tablename to store the places.
    city_id(str): city id of the place.
    user_id(str): user id of the place.
    name(str): name of the place.
    description(str): description of the place.
    number_rooms(int): Total no. of rooms of the place.
    number_bathrooms(int): Total no. of bathrooms of the place.
    max-guest(int): maximum no. of guests allowed.
    price_by_night(int): price of the place per night.
    latitude(float): the place's latitude.
    longitude(float): the place's longitude.
    """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
