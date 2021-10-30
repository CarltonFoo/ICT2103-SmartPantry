import os
import pandas as pd

class csv:
    """A CSV object represent the CSV."""
    def __init__(self, file: str) :
        if not file.endswith('.csv'):
            raise Exception("File format is not supported. Only supports CSV.")
        dir = os.path.join(os.getcwd(), "backend/datasets/", file)
        if not os.path.exists(dir):
            raise Exception("File does not exist in datasets folder")
        self.dir = dir
        self.dirname, self.filname= os.path.split(self.dir)
        self.data = self.import_csv()

    def  import_csv(self):
        """This imports CSV and returns a dataframe, expecting columns header"""
        return pd.read_csv(self.dir)