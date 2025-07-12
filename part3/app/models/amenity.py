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

    def add_place(self, place):
        """Add a place to the amenity."""
        self.places.append(place)
