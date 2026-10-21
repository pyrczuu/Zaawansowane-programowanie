class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"A property at {self.address} priced at {self.price } with {self.rooms} rooms, an area of {self.area}"