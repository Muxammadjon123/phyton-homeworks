import sqlite3


with sqlite3.connect('roster.db') as conn:
    cursor = conn.cursor()

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    ''')

   
    characters = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", characters)

    
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

   
    print("Bajoran characters:")
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    for row in cursor.fetchall():
        print(row)

    
    cursor.execute("DELETE FROM Roster WHERE Age > 100")

    
    try:
        cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    except sqlite3.OperationalError:
        pass

    
    ranks = [
        ("Captain", "Benjamin Sisko"),
        ("Lieutenant", "Ezri Dax"),
        ("Major", "Kira Nerys")
    ]
    for rank, name in ranks:
        cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))

  
    print("\nCharacters sorted by Age (desc):")
    cursor.execute("SELECT Name, Species, Age, Rank FROM Roster ORDER BY Age DESC")
    for row in cursor.fetchall():
        print(row)
