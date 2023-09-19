#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import relationship


class State(BaseModel, Base):
    """ The class State representation of MySql Database.

    Inherits from SQLAlchemy Base and links to the MySql table states.

    Attributes:
    __tablename__(str): Table name to store states
    name(str): The name of the state.
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref= "state", cascade= "delete")
