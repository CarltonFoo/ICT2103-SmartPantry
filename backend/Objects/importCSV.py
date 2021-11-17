import os
import pandas as pd
# from sqlalchemy import create_engine

class csv:
    """A CSV object represent the CSV."""
    def __init__(self, file: str) :
        if not file.endswith('.csv'):
            raise Exception("File format is not supported. Only supports CSV.")        
        dir = os.path.join(os.path.dirname(__file__), "../datasets/", file)
        if not os.path.exists(dir):
            raise Exception("File does not exist in datasets folder")
        self.dir = dir
        self.dirname, self.filname= os.path.split(self.dir)
        self.data = self.import_csv()

    def  import_csv(self):
        """This imports CSV and returns a dataframe, expecting columns header"""
        return pd.read_csv(self.dir)

    def  csv_to_sql(self, con, table: str, ifExists = 'append', chunkSize = 1000):
        """This function inserts Pandas DataFrames into a Database"""
        self.data.to_sql(table, con,if_exists=ifExists, chunksize= chunkSize)


# engine = create_engine('sqlite://', echo=False)
# a = csv("AverageFoodPrices.csv")
# a.csv_to_sql(table="users", con=engine)