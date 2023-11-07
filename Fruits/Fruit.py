from abc import ABC, abstractmethod

# Define the abstract parent class 'Fruits'
class Fruits(ABC):
    def __init__(self, origin,color,taste):
        self.origin = origin
        self.color = color
        self.taste = taste

    @property
    @abstractmethod
    def season(self):
        pass

    @abstractmethod
    def price(self):
        pass

       

