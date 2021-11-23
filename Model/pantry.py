from base import Base

class Pantry(Base):
    def __init__(self, data) -> None:
        Base.__init__(data)
        if self.hasData(data, "uid", "fid", "weight"):
            self.__uid = data["uid"]
            self.__fid = data["fid"]
            self.__weight = data["weight"]

    def setUid(self, data):
        if self.hasData(data, "uid"):
            self.__uid = data["uid"]

    def setFid(self, data):
        if self.hasData(data, "fid"):
            self.__fid = data["fid"]

    def setWeight(self, data):
        if self.hasData(data, "weight"):
            self.__weight = data["weight"]

    def getUid(self):
        return {"uid": self.__uid}

    def getFid(self):
        return {"fid": self.__fid}

    def getWeight(self):
        return {"weight": self.__weight}

    def getter(self):
        return {**self.getID(), **self.getFid(), **self.getUid, **self.getWeight()}