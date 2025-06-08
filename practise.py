import sqlite3

with sqlite3.connect("students.db") as connection:
    cursor=connection.cursor()
    query="Create Table Students(fname text,lname text,age int)"
    data=cursor.execute(query)

with sqlite3.connect("students.db") as connection:
    cursor=connection.cursor()
    query="Insert into Students Values('Ali','Valiev',21)"
    data=cursor.execute(query)