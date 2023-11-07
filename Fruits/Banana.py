from Fruits.Fruit import Fruits

class Banana(Fruits):
    def __init__(self, origin,color,taste,nutrition):
        super().__init__(origin,color,taste)
        self.nutrition = nutrition

    def season(self):
         return f"It grows in all seasons"

    def price(self):
         return f"It costs around $10"
