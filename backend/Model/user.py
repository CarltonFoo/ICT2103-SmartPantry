from base import  Base, DataParserInterface

class _Credential(DataParserInterface):
    def __init__(self, data:dict) -> None:
        if self.hasData(data, "username", "password"):
            self.__username = data['username']
            self.__password = data['password']

    def setCredential(self, data:dict) -> None:
        if self.hasData(data, "username", "password"):
            if data['username'] is not None:
                self.__username = data['username']
            if data['password'] is not None:
                self.__password = data['password']

    def getCredential(self) -> dict:
        return {"username": self.__username, "password":self.__password}

class _Demographic:
    def __init__(self, data) -> None:
        if self.hasData(data, "age", "gender", "height"):
            self.__age = data["age"]
            self.__gender = data["gender"]
            self.__height = data["height"]

    def setDemographic(self, data) -> None:
        self.__age = data["age"]
        self.__gender = data["gender"]
        self.__height = data["height"]

    def getDemographic(self) ->dict:
        return {"age": self.__age, "gender": self.__gender, "height": self.__height}

class User(Base, _Credential, _Demographic):
    def __init__(self,data) -> None:
        Base.__init__(self, data)
        _Credential.__init__(self, data)
        _Demographic.__init__(self, data)
        # print(self.__demographic.getDemographic())

    def getter(self):
        return {**self.getID(), **self.getCredential(), ** self.getDemographic() }


data1 = {
    "_id" : "123",
    "username" : "456",
    "password" : "789",
    "age" : "10",
    "gender" : "male",
    "height" : float("167"),
}

usr = User(data1)
print(usr.getter())