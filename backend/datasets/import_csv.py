import os
import pandas as pd

class csv:
    """A CSV object represent the CSV"""
    def __init__(self, file: str) :
        if not file.endswith('.csv'):
            raise Exception("<File format> is not supported. Only supports CSV")
        self.dirname, self.filname= os.path.split(os.path.abspath(file))

    def  import_csv(file):
        """This imports CSV and returns a dataframe, expecting columns header"""
        return pd.read_csv(file)

a = csv("import_csv.py")