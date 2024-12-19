
import sqlite3


CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()



# Team Attributes: 
# name: string 
# mascot: string 
# city: string 
# year founded: int


class Team:
    
    pass


# Athlete Attributes: 
# name: string 
# college: string 
# position: string 
# team id: int


class Athlete:
    
    pass


# Brand Attributes: 
# name: string 
# category: string 
# country of origin: string


class Brand:
    
    pass


# Deal Attributes: 
# athlete fee: int 
# brand id: int 
# athlete id: string



class Deal:
    
    pass