from app.models.BaseModel import BaseModel
from sqlalchemy import Float, String
from sqlalchemy.orm import  mapped_column

class Place(BaseModel):
    __tablename__ = 'places'

    title = mapped_column(String(50), nullable=False)
    description = mapped_column(String(255), nullable=False)
    price = mapped_column(Float, nullable=False)
    latitude = mapped_column(Float, nullable=False)
    longitude = mapped_column(Float, nullable=False)

        
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities
    

    @property
    def price(self):
        """
        Get the place price.
        """
        return self.__price
    @price.setter
    def price(self, value):
        """
        Set the place price.
        """
        if value < 0:
            raise ValueError(
                'The price should be a non-negative float.'
                )
        self.__price = value
    
    @property
    def latitude(self):
        """
        Get the place latitude.
        """
        return self.__latitude
        
    @latitude.setter
    def latitude(self, value):
        """
        Set the place latitude.
        """
        if value < -90 or value > 90:
            raise ValueError(
                'The latitude should be between -90 and 90.'
                )
        self.__latitude = value
    
    @property
    def longitude(self):
        """
        Get the place longitude.
        """
        return self.__longitude
        
    @longitude.setter
    def longitude(self, value):
        """
        Set the place longitude.
        """
        if value < -180 or value > 180:
            raise ValueError(
                'The longitude should be between -180 and 180.'
                )
        self.__longitude = value
        
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
