from app.models.BaseModel import BaseModel
from sqlalchemy import Float, String
from sqlalchemy.orm import  mapped_column

class Review(BaseModel):
    __tablename__ = 'reviews'

    text = mapped_column(String(255), nullable=False)
    rating = mapped_column(Float, nullable=False)
        
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
    @property
    def rating(self):
        """The rating property."""
        return self.__rating
    @rating.setter
    def rating(self, value):
        if value  < 1 or value > 5:
            raise ValueError(
                'The rating should be a between 11 and 5'
                )
        self.__rating = value
    
    @property
    def text(self):
        """The text property."""
        return self.__text
    @text.setter
    def text(self, value):
        self.__text = value
    
    @property
    def place_id(self):
        """The place_id property."""
        return self.__place_id
    @place_id.setter
    def place_id(self, value):
        self.__place_id = value
