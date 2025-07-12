from app.models.BaseModel import BaseModel
from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship


class Review(BaseModel):
    __tablename__ = 'reviews'

    text = mapped_column(String(255), nullable=False)
    rating = mapped_column(Float, nullable=False)
    user_id = mapped_column(String(36), ForeignKey('users.id'), nullable=False)
    place_id = mapped_column(String(36), ForeignKey('places.id'), nullable=False)
    
    user = relationship("User", back_populates="users")
    place = relationship("Place", back_populates="places")

        
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
