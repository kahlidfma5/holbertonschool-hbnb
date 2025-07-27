from app.models.BaseModel import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, validates, relationship
from app.models.place_amenity import Place_Amenity

class Amenity(BaseModel):

    __tablename__ = 'amenities'

    name = mapped_column(String(50), nullable=False)
    places_amenities = relationship("Place_Amenity", back_populates="amenity", cascade="all, delete-orphan")
 
        
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    @validates('name')
    def validate_name(self, key, name):
        """Validate that the name is not empty."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Amenity name cannot be empty")
        if len(name) > 50:
            raise ValueError("Amenity name must be less than 50 characters long")
        return name.strip()

    def add_place(self, place):
        """Add a place to the amenity."""
        self.places.append(place)
