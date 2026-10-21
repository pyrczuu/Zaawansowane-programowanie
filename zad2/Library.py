class Library:
    def __init__(self, city: str, street: str, zipcode: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zipcode = zipcode
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"{self.city}, {self.street}, {self.zipcode}, {self.open_hours}, {self.phone}"