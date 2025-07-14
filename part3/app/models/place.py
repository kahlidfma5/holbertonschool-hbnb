from app.models.BaseModel import BaseModel
from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import mapped_column, relationship, validates


class Place(BaseModel):
    __tablename__ = 'places'

    title = mapped_column(String(50), nullable=False)
    description = mapped_column(String(255), nullable=False)
    price = mapped_column(Float, nullable=False)
    latitude = mapped_column(Float, nullable=False)
    longitude = mapped_column(Float, nullable=False)
    owner_id = mapped_column(String(36), ForeignKey('users.id'), nullable=False)

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

    @validates('price')
    def validate_price(self, key, value):
        """Validate the price value."""
        if value < 0:
            raise ValueError('The price should be a non-negative float.')
        return value

    @validates('latitude')
    def validate_latitude(self, key, value):
        """Validate the latitude value."""
        if value < -90 or value > 90:
            raise ValueError('The latitude should be between -90 and 90.')
        return value

    @validates('longitude')
    def validate_longitude(self, key, value):
        """Validate the longitude value."""
        if value < -180 or value > 180:
            raise ValueError('The longitude should be between -180 and 180.')
        return value

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
