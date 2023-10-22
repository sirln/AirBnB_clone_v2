#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    '''
     The class State representation of MySql Database.

    Inherits from SQLAlchemy Base and links to the MySql table states.

    Attributes:
    __tablename__(str): Table name to store states
    name(str): The name of the state.
    '''

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
                            "City",
                            backref="state",
                            cascade="all, delete, delete-orphan"
                        )

    @property
    def cities(self):
        '''
        Getter attribute cities for FileStorage
        '''
        all_cities = models.storage.all(City)
        state_cities = []
        for city in all_cities.values():
            if city.state_id == self.id:
                state_cities.append(city)
        return (state_cities)
