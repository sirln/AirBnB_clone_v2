#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """ The class User representation of MySql Database.

    Inherits from SQLAlchemy Base and links to the MySql table users.

    Attributes:
    __tablename__(str): Table name to store users.
    email(str): The email of the user.
    password(str): The passwords of the user.
    first_name(str): The first name of the user.
    last_name(str): The last name of the user.
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    '''
    places = relationship(
                            "Place",
                            backref="user",
                            cascade="all, delete, delete-orphan"
                         )
    reviews = relationship(
                            "Review",
                            backref="user",
                            cascade="all, delete, delete-orphan"
                          )
    '''
