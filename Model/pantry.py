from Model.base import PantryItem
from base import Base, PantryItem

class Pantry(Base, PantryItem):
    
    def __init__(self, data:dict) -> None:

        if self.hasData(data, "uid", "fid","weight"):
            self.__uid = int(data["uid"])
            self.__fid = int(data["fid"])
            self.__weight= float(data["weight"])

    def setPantry(self, data:dict):
            if self.hasData(data, "uid", "fid", "weight"):
                self.__weight = float(data["weight"])

    def getPantry(self) ->dict:
        """Return all attributes data in type dict"""
        return {"uid":self.__uid, "fid":self.__fid, "weight":self.__weight}