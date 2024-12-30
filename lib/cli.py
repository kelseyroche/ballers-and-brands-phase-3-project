from lib.models import Team, Athlete, Brand, Deal, initialize_database

def main_menu():
    print("\nWelcome to the WNBA Management CLI!")
    print("""
______      ____     _____       _____        _____   ______      _____                                   
(_   _ \    (    )   (_   _)     (_   _)      / ___/  (   __ \    / ____\                                  
  ) (_) )   / /\ \     | |         | |       ( (__     ) (__) )  ( (___                                    
  \   _/   ( (__) )    | |         | |        ) __)   (    __/    \___ \                                   
  /  _ \    )    (     | |   __    | |   __  ( (       ) \ \  _       ) )                                  
 _) (_) )  /  /\  \  __| |___) ) __| |___) )  \ \___  ( ( \ \_))  ___/ /                                   
(______/  /__(  )__\ \________/  \________/    \____\  )_) \__/  /____/                                    
                                                                                                           
   ____        __      _   ______        ______    ______       ____        __      _   ______      _____  
  (    )      /  \    / ) (_  __ \      (_   _ \  (   __ \     (    )      /  \    / ) (_  __ \    / ____\ 
  / /\ \     / /\ \  / /    ) ) \ \       ) (_) )  ) (__) )    / /\ \     / /\ \  / /    ) ) \ \  ( (___   
 ( (__) )    ) ) ) ) ) )   ( (   ) )      \   _/  (    __/    ( (__) )    ) ) ) ) ) )   ( (   ) )  \___ \  
  )    (    ( ( ( ( ( (     ) )  ) )      /  _ \   ) \ \  _    )    (    ( ( ( ( ( (     ) )  ) )      ) ) 
 /  /\  \   / /  \ \/ /    / /__/ /      _) (_) ) ( ( \ \_))  /  /\  \   / /  \ \/ /    / /__/ /   ___/ /  
/__(  )__\ (_/    \__/    (______/      (______/   )_) \__/  /__(  )__\ (_/    \__/    (______/   /____/  
        """)
    while True:
        print("\nMain Menu:")
        print("1. View Brands")
        print("2. View Teams")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_brands()
        elif choice == "2":
            view_teams()
        elif choice == "3":
            print("Goodbye! Keep reaching for the stars!")
            break
        else:
            print("Invalid choice. Please try again.")

def view_brands():
    brands = Brand.get_all()
    print("""
           ____|
        o  \%/ |~~\
  o//              |
  8                |
 / >               |
~ ~             ~~~~~~
          """)
    print("\nViewing All Brands:")
    for brand in brands:
        print(f"{brand.id}: {brand.name}")

    while True:
        print("\nOptions:")
        print("1. View Brand Deals")
        print("2. Main Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            brand_id = input("Enter Brand ID to view deals: ")
            view_brand_deals(brand_id)
        elif choice == "2":
            return
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def view_brand_deals(brand_id):
    print("""
o- - -  \o          __|
   o/   /|          vv`\
  /|     |              |
   |    / \_            |
  / \   |               |
 /  |                   |
          """)
    brand = Brand.find_by_id(brand_id)
    if not brand:
        print("Brand not found.")
        return

    print(f"\nViewing Deals for {brand.name}:")
    deals = [deal for deal in Deal.get_all() if deal.brand_id == int(brand_id)]
    for deal in deals:
        athlete = Athlete.find_by_id(deal.athlete_id)
        print(f"Deal ID: {deal.id}, Athlete: {athlete.name}, Fee: {deal.athlete_fee}")

    while True:
        print("\nOptions:")
        print("1. View Brands")
        print("2. Main Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            return
        elif choice == "2":
            main_menu()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def view_teams():
    print("""
|__  o\
| W    \O
|       |\_
|      /-\
|    /     \
|
|
          """)
    teams = Team.get_all()
    print("\nViewing All Teams:")
    for team in teams:
        print(f"{team.id}: {team.name}")

    while True:
        print("\nOptions:")
        print("1. View Team Roster")
        print("2. Main Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            team_id = input("Enter Team ID to view roster: ")
            view_team_roster(team_id)
        elif choice == "2":
            return
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def view_team_roster(team_id):
    print("""
    o      |   __   |
      \_ O |  |__|  |
   ____/ \ |___WW___|
   __/   /     ||
               ||
               ||
_______________||________________
          """)
    team = Team.find_by_id(team_id)
    if not team:
        print("Team not found.")
        return

    print(f"\nViewing Roster for {team.name}:")
    athletes = [athlete for athlete in Athlete.get_all() if athlete.team_id == int(team_id)]
    for athlete in athletes:
        print(f"Athlete ID: {athlete.id}, Name: {athlete.name}")

    while True:
        print("\nOptions:")
        print("1. View Athlete")
        print("2. Draft a New Athlete")
        print("3. View Teams")
        print("4. Main Menu")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            athlete_id = input("Enter Athlete ID to view details: ")
            view_athlete(athlete_id)
        elif choice == "2":
            draft_new_athlete(team_id)
        elif choice == "3":
            return
        elif choice == "4":
            main_menu()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def view_athlete(athlete_id):
    print("""
|__  o\
| W    \O
|       |\_         |\
|      /-\           \O
|    /     \          |
|                    /|
|                   |  \
          """)
    athlete = Athlete.find_by_id(athlete_id)
    if not athlete:
        print("Athlete not found.")
        return

    print(f"\nViewing Athlete: {athlete.name}")
    deals = [deal for deal in Deal.get_all() if deal.athlete_id == int(athlete_id)]
    for deal in deals:
        brand = Brand.find_by_id(deal.brand_id)
        print(f"Deal ID: {deal.id}, Brand: {brand.name}, Fee: {deal.athlete_fee}")

    while True:
        print("\nOptions:")
        print("1. Add a New Deal")
        print("2. View Roster")
        print("3. Main Menu")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_deal(athlete_id)
        elif choice == "2":
            team_id = athlete.team_id
            view_team_roster(team_id)
        elif choice == "3":
            main_menu()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def draft_new_athlete(team_id):
    name = input("Enter Athlete Name: ")
    college = input("Enter College: ")
    position = input("Enter Position: ")
    Athlete.create(name, college, position, team_id)
    print("Athlete drafted successfully!")

def add_new_deal(athlete_id):
    brand_id = input("Enter Brand ID: ")
    athlete_fee = input("Enter Athlete Fee: ")
    Deal.create(athlete_fee, athlete_id, brand_id)
    print("Deal added successfully!")

def exit_program():
    print("Goodbye! Keep on ballin'!")
    exit()

if __name__ == "__main__":
    initialize_database()
    main_menu()

#      print("""
# ______      ____     _____       _____        _____   ______      _____                                   
# (_   _ \    (    )   (_   _)     (_   _)      / ___/  (   __ \    / ____\                                  
#   ) (_) )   / /\ \     | |         | |       ( (__     ) (__) )  ( (___                                    
#   \   _/   ( (__) )    | |         | |        ) __)   (    __/    \___ \                                   
#   /  _ \    )    (     | |   __    | |   __  ( (       ) \ \  _       ) )                                  
#  _) (_) )  /  /\  \  __| |___) ) __| |___) )  \ \___  ( ( \ \_))  ___/ /                                   
# (______/  /__(  )__\ \________/  \________/    \____\  )_) \__/  /____/                                    
                                                                                                           
#    ____        __      _   ______        ______    ______       ____        __      _   ______      _____  
#   (    )      /  \    / ) (_  __ \      (_   _ \  (   __ \     (    )      /  \    / ) (_  __ \    / ____\ 
#   / /\ \     / /\ \  / /    ) ) \ \       ) (_) )  ) (__) )    / /\ \     / /\ \  / /    ) ) \ \  ( (___   
#  ( (__) )    ) ) ) ) ) )   ( (   ) )      \   _/  (    __/    ( (__) )    ) ) ) ) ) )   ( (   ) )  \___ \  
#   )    (    ( ( ( ( ( (     ) )  ) )      /  _ \   ) \ \  _    )    (    ( ( ( ( ( (     ) )  ) )      ) ) 
#  /  /\  \   / /  \ \/ /    / /__/ /      _) (_) ) ( ( \ \_))  /  /\  \   / /  \ \/ /    / /__/ /   ___/ /  
# /__(  )__\ (_/    \__/    (______/      (______/   )_) \__/  /__(  )__\ (_/    \__/    (______/   /____/  
#         """)