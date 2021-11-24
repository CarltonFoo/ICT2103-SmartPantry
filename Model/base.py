from abc import abstractmethod
import json

class DataParserInterface:
    """Control class that has all operations needed for data parsing"""
    def hasData(self, data: dict, *args, selection:str = "all") -> bool:
        """Validate if data holding all/any keys"""
        if selection == "all":
            if all(key in data for key in args):
                return True
            else:
                raise KeyError(f'Parameter has missing {args}')
        elif selection == "any":
            if any(key in data for key in args):
                return True
            else:
                raise KeyError(f'Parameter has missing {args}')
        else:
            raise ValueError(f'selection has no {selection}')


    def getJSON(self, jsonData):
        try:
            # Parse JSON from String
            return json.loads(jsonData)
        except ValueError as err:
            return False


class Base(DataParserInterface):
    "Class contains attribute id"
    def __init__(self, data) -> None:
        if self.hasData(data, "_id"):
            self.__id = data["_id"]

    def getID(self):
        return {"_id": self.__id}

    def setID(self, data)->None:
        if self.hasData(data, "_id"):
            self.__id = data["_id"]
            
    @abstractmethod
    def getter(self):
        # Abstract getter method for all its children
        pass

class Item(DataParserInterface):
    """Class contains attribute name"""
    def __init__(self, data) -> None:
        if self.hasData(data, "name"):
            self.__name = data["name"]

    def getName(self):
        return {"name": self.__name}

    def setName(self,data):
        if self.hasData(data, "name"):
            self.__id = data["name"]
