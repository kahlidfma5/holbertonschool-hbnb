from typing import List
from app.models.BaseModel import BaseModel
from flask_bcrypt import Bcrypt
from sqlalchemy import Boolean, String
from sqlalchemy.orm import mapped_column, validates
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

    @validates('email')
    def validate_email(self, key, email):
        """Validate the email format."""
        if not isinstance(email, str) or '@' not in email:
            raise ValueError("Valid email is required")
        return email

    @validates('first_name', 'last_name')
    def validate_name(self, key, name):
        """Validate that names are not empty."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"{key.replace('_', ' ').title()} cannot be empty")
        if not name or len(name) > 50 or len(name) < 1:
            raise ValueError(
                'The last name must be indicated and must be less than 50 characters long.'
                )
        return name.strip()

    def hash_password(self, password):
        """Hash the password before storing it."""
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verify the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
