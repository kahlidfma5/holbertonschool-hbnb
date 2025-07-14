from app.models.BaseModel import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import mapped_column
from app.database import db
from app.models.place_amenity import Place_Amenity

class Amenity(BaseModel):

    __tablename__ = 'amenities'

    name = mapped_column(String(50), nullable=False)
    places_amenities = db.relationship("Place_Amenity", back_populates="amenity", cascade="all, delete-orphan")
 
        
    def __init__(self, name):
        super().__init__()
        self.name = name

    def add_place(self, place):
        """Add a place to the amenity."""
        self.places.append(place)
