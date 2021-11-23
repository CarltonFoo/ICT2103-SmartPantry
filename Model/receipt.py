from Model.base import Base
from Model.food_item import food_item


class Receipt(Base):
    """Class inherited from Base and contains addition attributes list(food_item)"""
    def __init__(self, data) -> None:
        Base.__init__(self, data)
        if self.hasData(data, "uid", "fid"):
            self.__uid = data["uid"]
            self.__fid = data["fid"]

    def getIngredient(self):
        """Return all attributes of ingredients in type dict"""
        ingredientsList = []
        for item in self.__ingredients:
            ingredientsList.append(item.getter())
        return {"ingredients": ingredientsList}

    def getter(self):
        """Return all attributes data in type dict"""
        return {**self.getID(),**self.getIngredient()}
