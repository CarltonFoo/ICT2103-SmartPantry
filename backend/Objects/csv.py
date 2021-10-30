import os
import pandas as pd

class csv:
    """A CSV object represent the CSV."""
    def __init__(self, file: str) :
        script_dir = os.path.dirname(__file__)
        self.dir = os.path.join(script_dir, "../datasets/" + file)
        if not file.endswith('.csv'):
            raise Exception("<File format> is not supported. Only supports CSV file format and ensure file is stored in datasets folder")
        self.dirname, self.filname= os.path.split(os.path.abspath(self.dir))
        self.data = self.import_csv()

    def  import_csv(self):
        """This imports CSV and returns a dataframe, expecting columns header"""
        return pd.read_csv(self.dir)