import os
import pandas as pd
# from sqlalchemy import create_engine

class CSV:
    """A CSV object represent the CSV."""
    def __init__(self, file: str) :
        if not file.endswith('.csv'):
            raise Exception("File format is not supported. Only supports CSV.")
        dir = os.path.join(os.path.dirname(__file__), "../datasets/", file)
        if not os.path.exists(dir):
            raise Exception("File does not exist in datasets folder")
        # Absolute Directory
        self.dir = dir
        # Directory name and file name
        self.dirname, self.filname= os.path.split(self.dir)
        # Dataframe
        self.df = self.import_csv()

    def  import_csv(self):
        """This imports CSV and returns a dataframe, expecting columns header"""
        return pd.read_csv(self.dir, encoding='cp1252')

    def  csv_to_sql(self, con, table: str, ifExists = 'append', chunkSize = 1000):
        """This function inserts Pandas DataFrames into a Database"""
        self.df.to_sql(table, con,if_exists=ifExists, chunksize= chunkSize)

# engine = create_engine('sqlite://', echo=False)
# a = CSV("AverageFoodPrices.csv")
# b = CSV("FoodReceipes.csv")

# print(a.df)
# print(b.df)
# a.csv_to_sql(table="users", con=engine)