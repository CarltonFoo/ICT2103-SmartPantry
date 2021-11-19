from Model.base import Base
from Model.food_item import food_item


class receipt(Base):
    """Class inherited from Base and contains addition attributes list(food_item)"""
    def __init__(self, jsonData) -> None:
        data = self.getJSON(jsonData=jsonData)
        self.__ingredients = []
        if data is  False:
            raise TypeError("Parsed data is not in JSON format")
        Base.__init__(self, data)
        for item in data["ingredient"]:
            self.__ingredients = self.__ingredients.append(food_item(data))

    def getIngredient(self):
        """Return all attributes of ingredients in type dict"""
        ingredientsList = []
        for item in self.__ingredients:
            ingredientsList.append(item.getter())
        return {"ingredients": ingredientsList}

    def getter(self):
        """Return all attributes data in type dict"""
        return {**self.getID(),**self.getIngredient()}
