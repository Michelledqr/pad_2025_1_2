import pandas as pd
import sqlite3
import os

class DataBase:
    def __init__(self):
        self.pathdb = "src/static/db/currency.db"

    def save_df(self,df=pd.DataFrame()):
        df = df.copy()
        try:
            conn = sqlite3.connect(self.pathdb)
            df["date_create"]= "2025-05-21"
            df["date_update"] = "2025-05-21"
            print (df.head())
            df.to_sql("currency_db",conn,if_exists='replace',index=False)
            print(f"Currency DB - saved! {df.shape[0]} records.")
            conn.close
        except Exception as errores:
            print("Error recording dataframe to DB!")

    def get_data(self,nombre_tabla=""):
        try:
            conn = sqlite3.connect(self.pathdb)
            consulta = "select * from {}".format(nombre_tabla)
            df = pd.read_sql_query(consulta,conn)
            print("# of records at DB {}".format(df.shape[0]))
            return df
        except Exception as errores:
            print("Error reading Database {str(nombre_tabla)}: {str(errores)}")
            return df
            

"""
data = {"ID": [1, 2, 3], "Nombre": ["Aaaa", "Bbb", "Ccc"], "Edad": [25, 30, 35]}
df = pd.DataFrame(data)
db=DataBase()
db.save_df(df)
"""