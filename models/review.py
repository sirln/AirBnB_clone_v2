#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ The class Review representation of MySql Database.

    Inherits from SQLAlchemy Base and links to the MySql table reviews.

    Attributes:
    __tablename__(str): the name of the MySQL table to store Reviews.
    text(str): the description of the review.
    place_id(str): the review's place id.
    user_id(str): the review's user id.
    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
