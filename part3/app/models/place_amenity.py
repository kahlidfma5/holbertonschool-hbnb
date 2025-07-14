from app.models.BaseModel import BaseModel
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, relationship

class Place_Amenity(BaseModel):

    __tablename__ = 'places_amenities'

    amenity_id = mapped_column(String(36), ForeignKey('amenities.id'), primary_key=True)
    place_id = mapped_column(String(36), ForeignKey('places.id'), primary_key=True)

    place = relationship("Place", back_populates="places_amenities")
    amenity = relationship("Amenity", back_populates="places_amenities")

