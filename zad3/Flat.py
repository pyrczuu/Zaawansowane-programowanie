from zad3.Property import Property

class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: float):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f" and a floor of {self.floor}"