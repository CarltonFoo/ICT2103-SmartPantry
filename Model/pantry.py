from Model.base import PantryItem
from base import Base, PantryItem

class Pantry(Base, PantryItem):
    
    def __init__(self, uid, fid, weight) -> None:

        if self.hasData(uid, fid, weight):
            self.__uid = uid
            self.__fid = fid
            self.__weight=weight

    def setPantry(self, weight):
            self.__weight = weight
    def getter(self):
        """Return all attributes data in type dict"""
        return {**self.__uid(), **self.__fid(), **self.__weight()}