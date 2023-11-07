from Fruits.Fruit import Fruits

class Apple(Fruits):
    def __init__(self, origin,color,taste,texture):
        super().__init__(origin,color,taste)
        self.texture = texture

    def season(self):
         return f"It grows in Winter seaason"

    def price(self):
         return f"It costs around $80"
