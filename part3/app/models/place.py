from app.models.BaseModel import BaseModel
from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import mapped_column, relationship


class Place(BaseModel):
    __tablename__ = 'places'

    title = mapped_column(String(50), nullable=False)
    description = mapped_column(String(255), nullable=False)
    price = mapped_column(Float, nullable=False)
    latitude = mapped_column(Float, nullable=False)
    longitude = mapped_column(Float, nullable=False)
    user_id = mapped_column(String(36), ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="places")
    reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")
    places_amenities = relationship("Place_Amenity", back_populates="place", cascade="all, delete-orphan")


        
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id


    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
