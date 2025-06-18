class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.places = []  # List to store related amenities

    def add_place(self, place):
        """Add a place to the amenity."""
        self.places.append(place)
