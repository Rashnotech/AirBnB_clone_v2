#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, Float, String, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    amenities = relationship('Amenity', secondary='place_amenity',
        viewonly=False, backref='places')

    @property
    def amenities(self):
        """ getter instance method """
        from models import storage
        amenities_list = []
        for amenity_id in self.amenity_ids:
            amenity = storage.all(Amenity)
            if amenity_id in amenity:
                amenities_list.append(amenity)
        return amenities_list

    @amenities.setter
    def amenities(self, obj):
        """ a setter instance method """
        if isinstance(obj, Amenity):
            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)

    def append_amenity(self, amenity_id):
        """ method to append amenity.id to amenity_ids """
        if amenity_id not in self.amenity_ids:
            self.amenity_ids.append(amenity_id)

