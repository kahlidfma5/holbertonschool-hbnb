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
