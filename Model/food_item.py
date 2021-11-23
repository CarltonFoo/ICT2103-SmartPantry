from Model.base import Item
from base import Base, Item

class Food_item(Base, Item):
    """Class inherited Base, Item and contains an additional attribute price"""
    def __init__(self, data) -> None:
        Base.__init__(data)
        Item.__init__(data)
        if self.hasData(data, "price", "weight"):
            self.__price = float(data["price"])
            self.__weight = int(data["weight"])

    def setFoodItem(self, data):
        self.setID(data)
        self.setName(data)
        if self.hasData(data, "price"):
            self.__price = float(data["price"])
        if self.hasData(data, "weight"):
            self.__weight = int(data["weight"])
    
    def getPrice(self):
        return {"price", self.__price}

    def getWeight(self):
        return {"weight", self.__weight}

    def getter(self):
        """Return all attributes data in type dict"""
        return {**self.getID(), **self.getName(), **self.getPrice(), **self.getWeight()}