WNBA Database Management Project

Overview

This project is a Python-based application for managing a database of WNBA teams, athletes, brands, and endorsement deals. It demonstrates core programming concepts, including object-oriented programming (OOP), database interactions with SQLite, and command-line interface (CLI) functionality. Users can draft new athletes, sign endorsement deals, and explore team and athlete data.

Features
	•	Draft New Players: Add athletes to teams with their personal and career details.
	•	Sign Endorsement Deals: Create brand deals associated with athletes.
	•	Database Management: Create and manage database tables for teams, athletes, brands, and deals.
	•	Data Relationships: Leverage relationships between data models, such as teams and athletes or brands and deals.
	•	Interactive CLI: A simple interface for interacting with the database.

Technologies Used
	•	Python: Programming language for application logic and database interactions.
	•	SQLite: Relational database for storing and managing data.
	•	Pipenv: Dependency and virtual environment manager.

Data Model
	•	Team: Contains team-specific details and has many athletes.
	•	Athlete: Contains player-specific details and belongs to a team. May have multiple endorsement deals.
	•	Brand: Represents companies offering endorsement deals.
	•	Deal: Represents an endorsement contract between a brand and an athlete.

Relationships:
	•	A Team can have many Athletes, but each Athlete belongs to one Team.
	•	A Brand can have many Deals, but each Deal belongs to one Brand.
	•	An Athlete can have many Deals, but each Deal is tied to one Athlete.

Setup Instructions
	1.	Clone the repository:

git clone https://github.com/your-repository-url.git
cd your-repository


	2.	Set up a virtual environment:

pipenv install
pipenv shell


	3.	Initialize the database:
Run the project once to generate the SQLite database and tables:

python main.py

Usage
	1.	Run the application:

python main.py


	2.	Available CLI Commands:
	•	1 - Draft a new athlete.
	•	2 - Sign a new endorsement deal.
	•	3 - View all teams, athletes, or deals.
	•	4 - Exit the application.
	3.	Follow the prompts to interact with the database and perform actions.

Code Highlights
	•	Instance Method:

def save(self):
    conn, cursor = Database.get_connection()
    cursor.execute(
        f"INSERT INTO {self.__tablename__} (name, college, position, team_id) VALUES (?, ?, ?, ?)",
        (self.name, self.college, self.position, self.team_id),
    )
    conn.commit()
    Database.close_connection(conn)

The save method saves an athlete’s data to the database.

	•	Class Method:

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

The create_table method initializes the database table for a class.

Future Features
	•	Add search functionality to filter athletes or deals based on user-defined criteria.
	•	Enhance the CLI with more user-friendly commands.
	•	Integrate API endpoints for external data sources, such as WNBA stats or brand partnerships.

Contributing
	1.	Fork the repository.
	2.	Create a new branch for your feature:

git checkout -b feature-name


	3.	Commit your changes:

git commit -m "Add feature-name"


	4.	Push the changes to your branch:

git push origin feature-name


	5.	Create a pull request.

License

This project is licensed under the MIT License.

Let me know if you’d like to make any specific adjustments or add more details!