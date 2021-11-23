from base import Base

class MealHistory(Base):
    def __init__(self, data) -> None:
        Base.__init__(data)
        if self.hasData(data, "date", "meal_type", "rid", "uid"):
            self.__date = data["date"]
            self.__meal_type = data["meal_type"]
            self.__rid = data["rid"]
            self.__uid = data["uid"]

    def setDate(self, data):
        if self.hasData(data, "date"):
            self.__date = data["date"]

    def setMealType(self, data):
        if self.hasData(data, "meal_type"):
            self.__meal_type = data["meal_type"]

    def setRid(self, data):
        if self.hasData(data, "rid"):
            self.__rid = data["rid"]

    def setDate(self, data):
        if self.hasData(data, "uid"):
            self.__uid = data["uid"]

    def getDate(self, data):
        return {"date": self.__date}

    def getMealType(self, data):
        return {"meal_type": self.__meal_type}

    def getRid(self, data):
        return {"rid": self.__rid}

    def getUid(self, data):
        return {"uid": self.__uid}

    def getter(self):
        return {**self.getID(), **self.getDate, **self.getMealType(), **self.getRid(), **self.getUid()}
