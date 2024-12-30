import sqlite3

DATABASE = 'lib/wnba_project.db'  # Ensure this path is correct

class Database:
    """A simple class to manage database connections."""
    @staticmethod
    def get_connection():
        conn = sqlite3.connect(DATABASE)
        return conn, conn.cursor()

    @staticmethod
    def close_connection(conn):
        conn.close()

class Team:
    """Team model with attributes and relationships."""
    __tablename__ = "teams"

    def __init__(self, id, name, mascot, city, year_founded):
        self.id = id
        self.name = name
        self.mascot = mascot
        self.city = city
        self.year_founded = year_founded

    @classmethod
    def create_table(cls):
        conn, cursor = Database.get_connection()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {cls.__tablename__} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                mascot TEXT,
                city TEXT,
                year_founded INTEGER
            )
        """)
        conn.commit()
        Database.close_connection(conn)

    @classmethod
    def create(cls, name, mascot, city, year_founded):
        conn, cursor = Database.get_connection()
        cursor.execute(f"""
            INSERT INTO {cls.__tablename__} (name, mascot, city, year_founded)
            VALUES (?, ?, ?, ?)
        """, (name, mascot, city, year_founded))
        conn.commit()
        Database.close_connection(conn)

    @classmethod
    def get_all(cls):
        conn, cursor = Database.get_connection()
        cursor.execute(f"SELECT * FROM {cls.__tablename__}")
        rows = cursor.fetchall()
        Database.close_connection(conn)
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        conn, cursor = Database.get_connection()
        cursor.execute(f"SELECT * FROM {cls.__tablename__} WHERE id = ?", (id,))
        row = cursor.fetchone()
        Database.close_connection(conn)
        return cls(*row) if row else None

    @classmethod
    def delete(cls, id):
        conn, cursor = Database.get_connection()
        cursor.execute(f"DELETE FROM {cls.__tablename__} WHERE id = ?", (id,))
        conn.commit()
        Database.close_connection(conn)

class Athlete:
    """Athlete model with attributes and relationships."""
    __tablename__ = "athletes"

    def __init__(self, id, name, college, position, team_id):
        self.id = id
        self.name = name
        self.college = college
        self.position = position
        self.team_id = team_id

    @classmethod
    def create_table(cls):
        conn, cursor = Database.get_connection()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {cls.__tablename__} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                college TEXT,
                position TEXT,
                team_id INTEGER,
                FOREIGN KEY (team_id) REFERENCES teams (id)
            )
        """)
        conn.commit()
        Database.close_connection(conn)

    @classmethod
    def create(cls, name, college, position, team_id):
        conn, cursor = Database.get_connection()
        cursor.execute(f"""
            INSERT INTO {cls.__tablename__} (name, college, position, team_id)
            VALUES (?, ?, ?, ?)
        """, (name, college, position, team_id))
        conn.commit()
        Database.close_connection(conn)

    @classmethod
    def get_all(cls):
        conn, cursor = Database.get_connection()
        cursor.execute(f"SELECT * FROM {cls.__tablename__}")
        rows = cursor.fetchall()
        Database.close_connection(conn)
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        conn, cursor = Database.get_connection()
        cursor.execute(f"SELECT * FROM {cls.__tablename__} WHERE id = ?", (id,))
        row = cursor.fetchone()
        Database.close_connection(conn)
        return cls(*row) if row else None

    @classmethod
    def delete(cls, id):
        conn, cursor = Database.get_connection()
        cursor.execute(f"DELETE FROM {cls.__tablename__} WHERE id = ?", (id,))
        conn.commit()
        Database.close_connection(conn)

class Brand:
    """Brand model with attributes and relationships."""
    __tablename__ = "brands"

    def __init__(self, id, name, category, country_of_origin):
        self.id = id
        self.name = name
        self.category = category
        self.country_of_origin = country_of_origin

    @classmethod
    def create_table(cls):
        conn, cursor = Database.get_connection()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {cls.__tablename__} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                country_of_origin TEXT
            )
        """)
        conn.commit()
        Database.close_connection(conn)

    @classmethod
    def create(cls, name, category, country_of_origin):
        conn, cursor = Database.get_connection()
        cursor.execute(f"""
            INSERT INTO {cls.__tablename__} (name, category, country_of_origin)
            VALUES (?, ?, ?)
        """, (name, category, country_of_origin))
        conn.commit()
        Database.close_connection(conn)

    @classmethod
    def get_all(cls):
        conn, cursor = Database.get_connection()
        cursor.execute(f"SELECT * FROM {cls.__tablename__}")
        rows = cursor.fetchall()
        Database.close_connection(conn)
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        conn, cursor = Database.get_connection()
        cursor.execute(f"SELECT * FROM {cls.__tablename__} WHERE id = ?", (id,))
        row = cursor.fetchone()
        Database.close_connection(conn)
        return cls(*row) if row else None

    @classmethod
    def delete(cls, id):
        conn, cursor = Database.get_connection()
        cursor.execute(f"DELETE FROM {cls.__tablename__} WHERE id = ?", (id,))
        conn.commit()
        Database.close_connection(conn)

class Deal:
    """Deal model with attributes and relationships."""
    __tablename__ = "deals"

    def __init__(self, id, athlete_fee, athlete_id, brand_id):
        self.id = id
        self.athlete_fee = athlete_fee
        self.athlete_id = athlete_id
        self.brand_id = brand_id

    @classmethod
    def create_table(cls):
        conn, cursor = Database.get_connection()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {cls.__tablename__} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                athlete_fee INTEGER,
                athlete_id INTEGER,
                brand_id INTEGER,
                FOREIGN KEY (athlete_id) REFERENCES athletes (id),
                FOREIGN KEY (brand_id) REFERENCES brands (id)
            )
        """)
        conn.commit()
        Database.close_connection(conn)

    @classmethod
    def create(cls, athlete_fee, athlete_id, brand_id):
        conn, cursor = Database.get_connection()
        cursor.execute(f"""
            INSERT INTO {cls.__tablename__} (athlete_fee, athlete_id, brand_id)
            VALUES (?, ?, ?)
        """, (athlete_fee, athlete_id, brand_id))
        conn.commit()
        Database.close_connection(conn)

    @classmethod
    def get_all(cls):
        conn, cursor = Database.get_connection()
        cursor.execute(f"SELECT * FROM {cls.__tablename__}")
        rows = cursor.fetchall()
        Database.close_connection(conn)
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        conn, cursor = Database.get_connection()
        cursor.execute(f"SELECT * FROM {cls.__tablename__} WHERE id = ?", (id,))
        row = cursor.fetchone()
        Database.close_connection(conn)
        return cls(*row) if row else None

    @classmethod
    def delete(cls, id):
        conn, cursor = Database.get_connection()
        cursor.execute(f"DELETE FROM {cls.__tablename__} WHERE id = ?", (id,))
        conn.commit()
        Database.close_connection(conn)

def initialize_database():
    Team.create_table()
    Athlete.create_table()
    Brand.create_table()
    Deal.create_table()