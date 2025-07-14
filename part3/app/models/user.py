from typing import List
from app.models.BaseModel import BaseModel
from flask_bcrypt import Bcrypt
from sqlalchemy import Boolean, String
from sqlalchemy.orm import mapped_column
from app.database import db



bcrypt = Bcrypt()
class User(BaseModel):
    __tablename__ = 'users'

    first_name = mapped_column(String(255), nullable=False)
    last_name = mapped_column(String(255), nullable=False)
    email = mapped_column(String(255), nullable=False, unique=True)
    password = mapped_column(String(255), nullable=False)
    is_admin = mapped_column(Boolean, default=False)

    places = db.relationship("Place", back_populates="user", cascade="all, delete-orphan")
    reviews = db.relationship("Review", back_populates="user", cascade="all, delete-orphan")
        
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.hash_password(password)
        print(f'{password}->{self.password}')
        self.is_admin = is_admin
    
    def hash_password(self, password):
        """Hash the password before storing it."""
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verify the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
