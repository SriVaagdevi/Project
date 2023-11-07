from Fruits.Fruit import Fruits

class Cherry(Fruits):
    def __init__(self, origin,color,taste,availability):
        super().__init__(origin,color,taste)
        self.availability = availability

    def season(self):
         return f"It grows in spring and summer months"

    def price(self):
         return f"It costs around $50"
