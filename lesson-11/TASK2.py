import sqlite3

with sqlite3.connect('library2.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
    ''')
    
    data = [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ]
    cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", data)
    
    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
    
    print("Dystopian Books:")
    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    for row in cursor.fetchall():
        print(row)
    
    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
    
    try:
        cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    except sqlite3.OperationalError:
        pass
    
    ratings = [
        (4.8, "To Kill a Mockingbird"),
        (4.7, "1984"),
        (4.5, "The Great Gatsby")
    ]
    for rating, title in ratings:
        cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))
    
    print("\nBooks sorted by Year_Published:")
    cursor.execute("SELECT Title, Author, Year_Published, Genre, Rating FROM Books ORDER BY Year_Published ASC")
    for row in cursor.fetchall():
        print(row)

    conn.commit()
