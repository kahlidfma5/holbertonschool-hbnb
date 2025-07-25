from app.persistence.repository import SQLAlchemyRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

    def create_user(self, user_data):
        
        print(f'Facade User data:{user_data}')
        user = User(**user_data)
        print(f'Facade Password->{user.password}')
        self.user_repo.add(user)
        return user
    
    def update_user(self, user_id, user_data):
        if self.get_user(user_id):
            self.user_repo.update(user_id, user_data)

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        
        return self.user_repo.get_by_attribute('email', email)

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()
    
    def update_amenity(self, amenity_id, amenity_data):
        if self.get_amenity(amenity_id):
            self.amenity_repo.update(amenity_id, amenity_data)
    
    def create_place(self, place_data):
        place = Place(**place_data)
        #place.amenities = place_data['amenities']
        self.place_repo.add(place)
        return place 

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)
        
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review 

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        reviews = self.review_repo.get_all()
        return [review for review in reviews if review.place_id == place_id]

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)

