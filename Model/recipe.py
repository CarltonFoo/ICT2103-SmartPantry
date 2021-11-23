
from base import Base, Item

class Recipe(Base, Item):
    def __init__(self, data) -> None:
        Base.__init__(data)
        Item.__init__(data)
        if self.hasData(data, "calories", "description", "dietary_needs"):
            self.__calories = data["calories"]
            self.__description = data["description"]
            self.__dietary_needs = data["dietary_needs"]

    def setCalories(self, data):
        if self.hasData(data, "calories"):
            self.__calories = data["calories"]

    def setDescription(self, data):
        if self.hasData(data,  "description"):
            self.__description = data["description"]
        pass

    def setDeitaryNeeds(self, data):
        if self.hasData(data, "dietary_needs"):
            self.__dietary_needs = data["dietary_needs"]

    def getCalories(self):
        return {"calories", self.__calories}

    def getDescription(self):
        return {"description", self.__description}
        
    def getDietaryNeeds(self):
        return {"dietary_needs", self.__dietary_needs}

    def getter(self):
        return {**self.getID(), **self.getName(), **self.getCalories(), **self.getDescription(), **self.getDietaryNeeds()}