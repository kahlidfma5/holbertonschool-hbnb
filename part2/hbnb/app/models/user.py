class User(BaseModel):
    def __init__(self, first_name, last_name, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
