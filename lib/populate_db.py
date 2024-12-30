import sqlite3
import os

# Define the database path
DB_PATH = os.path.join(os.path.dirname(__file__), 'wnba_project.db')

# Connect to the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Define schema
cursor.execute('''
CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    mascot TEXT NOT NULL,
    city TEXT NOT NULL,
    year_founded INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS athletes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    college TEXT NOT NULL,
    position TEXT NOT NULL,
    team_id INTEGER NOT NULL,
    FOREIGN KEY(team_id) REFERENCES teams(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS brands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    country_of_origin TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS deals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    athlete_fee REAL NOT NULL,
    brand_id INTEGER NOT NULL,
    athlete_id INTEGER NOT NULL,
    FOREIGN KEY(brand_id) REFERENCES brands(id),
    FOREIGN KEY(athlete_id) REFERENCES athletes(id)
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO teams (name, mascot, city, year_founded)
VALUES (?, ?, ?, ?)
''', [
    ('Las Vegas Aces', 'Ace', 'Las Vegas', 1997),
    ('New York Liberty', 'Torch', 'New York', 1997),
    ('Seattle Storm', 'Doppler', 'Seattle', 2000),
])

cursor.executemany('''
INSERT INTO athletes (name, college, position, team_id)
VALUES (?, ?, ?, ?)
''', [
    ('A’ja Wilson', 'South Carolina', 'Forward', 1),
    ('Breanna Stewart', 'UConn', 'Forward', 2),
    ('Sue Bird', 'UConn', 'Guard', 3),
])

cursor.executemany('''
INSERT INTO brands (name, category, country_of_origin)
VALUES (?, ?, ?)
''', [
    ('Nike', 'Clothing', 'USA'),
    ('Adidas', 'Clothing', 'Germany'),
    ('Puma', 'Clothing', 'Germany'),
])

cursor.executemany('''
INSERT INTO deals (athlete_fee, brand_id, athlete_id)
VALUES (?, ?, ?)
''', [
    (500000, 1, 1),
    (450000, 2, 2),
    (300000, 3, 3),
])

# Commit and close
conn.commit()
conn.close()

print(f"Database populated successfully at {DB_PATH}")