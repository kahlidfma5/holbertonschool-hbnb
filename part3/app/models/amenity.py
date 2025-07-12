from app.models.BaseModel import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import  mapped_column
class Amenity(BaseModel):

    __tablename__ = 'amenities'

    name = mapped_column(String(50), nullable=False)
 
        
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.places = []  # List to store related amenities


    @property
    def name(self):
        """
        Get the amenity name.
        """
        return self.__name
        
    @name.setter
    def name(self, value):
        """
        Set the amenity name.
        """
        if not value or len(value) < 1 or len(value) > 50:
            raise ValueError(
                'The name field should be between 1 and 50 characters.'
                )
        self.__name = value

    def add_place(self, place):
        """Add a place to the amenity."""
        self.places.append(place)
