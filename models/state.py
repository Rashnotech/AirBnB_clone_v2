#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if storage_type == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """Getter attribute instance for FileStorage"""
        if storage_type != 'db':
            from models import storage
            return [city for city in storage.all('City').values()
                    if city.state_id == self.id]
