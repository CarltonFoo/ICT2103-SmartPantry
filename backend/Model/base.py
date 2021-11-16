from abc import abstractmethod
import json

class DataParserInterface:
    def hasData(self, data: dict, *args) -> bool:
        if all(key in data for key in args):
            return True
        else:
            raise ValueError(f'Parameter has missing {args}')

    def  validateJSON(self, jsonData):
        try:
            # Parse JSON from String
            json.loads(jsonData)
            # Parse JSON from file
            json.load(jsonData)
        except ValueError as err:
            return False
        return True


class Base(DataParserInterface):
    def __init__(self, data) -> None:
        if self.hasData(data, "_id"):
            self.__id = data["_id"]

    def getID(self):
        return {"_id": self.__id}
        
    @abstractmethod
    def getter(self):
        pass

