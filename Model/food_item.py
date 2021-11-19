from Model.base import Item
from base import Base, Item

class food_item(Base, Item):
    """Class inherited Base, Item and contains an additional attribute price"""
    def __init__(self, jsonData) -> None:
        data = self.getJSON(jsonData=jsonData)
        if data is  False:
            raise TypeError("Parsed data is not in JSON format")
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

    def getter(self):
        """Return all attributes data in type dict"""
        return {**self.getID(), **self.getName(), **{"price", self.__price}, **{"weight", self.__weight}}