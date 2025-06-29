import sqlite3
import pandas as pd

with sqlite3.connect('chinook.db') as con:
    df=pd.read_sql('SELECT * FROM customers',con)
    df.head(10)