
from dataweb import Dataweb
from database import DataBase
import pandas as pd

def main():
    dataweb = Dataweb()
    database = DataBase()
    
    df = dataweb.obtener_datos()
    print(df.head())
    df.rename(columns={'': 'idx'}, inplace=True)
    df.rename(columns={'%': 'Var_porc'}, inplace=True)
    df.drop(columns='idx',inplace=True)
    database.save_df(df)
    df_db2 = database.get_data("currency_db")
    df_db2.to_csv("src/edu_pad/static/db/DataInDatabase.csv", index=False)



if __name__ == "__main__":
    main()
