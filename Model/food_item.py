from Model.base import Item
from base import Base, Item

class food_item(Base, Item):
    def __init__(self, jsonData) -> None:
        data = self.getJSON(jsonData=jsonData)

        if data is  False:
            raise TypeError("Parsed data is not in JSON format")
        Base.__init__(data)
        Item.__init__(data)
        self.__price = data["price"]

    def getter(self):
        return {**self.getID(), **self.getName(), **{"price", self.__price}}