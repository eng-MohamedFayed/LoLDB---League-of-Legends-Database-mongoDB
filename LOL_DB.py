import pymongo
from datetime import datetime

# Establish connection to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["LOL"]  # Replace "LOL" with your database name

# Function to retrieve match history based on summoner name
def get_match_history(summoner_name):
    match_history = db.matchHistory.find({"summonerName": summoner_name})
    return list(match_history)

# Function to add a new match to the match history
def add_match(summoner_name, champion, result, kills, deaths, assists):
    match_id = db.matchHistory.count_documents({}) + 1
    new_match = {
        "matchId": match_id,
        "date": datetime.now(),
        "result": result,
        "summonerName": summoner_name,
        "champion": champion,
        "kills": kills,
        "deaths": deaths,
        "assists": assists
    }
    db.matchHistory.insert_one(new_match)
    print("Match added successfully!")

# Function to retrieve profiles based on summoner name
def get_profile(summoner_name):
    profile = db.profiles.find({"summonerName": summoner_name})
    return profile

# Function to add a new profile
def add_profile(summoner_name, level, server, main_champion):
    new_profile = {
        "summonerName": summoner_name,
        "level": level,
        "server": server,
        "mainChampion": main_champion
    }
    db.profiles.insert_one(new_profile)
    print("Profile added successfully!")

# Function to retrieve champions based on champion name
def get_champion(champion_name):
    champion = db.champions.find({"name": champion_name})
    return champion

# Function to add a new champion
def add_champion(name, champ_type, difficulty):
    new_champion = {
        "name": name,
        "type": champ_type,
        "difficulty": difficulty
    }
    db.champions.insert_one(new_champion)
    print("Champion added successfully!")

# Example usage
while True:
    print("1. Get Match History")
    print("2. Add Match")
    print("3. Get Profile")
    print("4. Add Profile")
    print("5. Get Champion")
    print("6. Add Champion")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        summoner_name = input("Enter summoner name: ")
        matches = get_match_history(summoner_name)
        for match in matches:
            print(match)
    
    elif choice == "2":
        summoner_name = input("Enter summoner name: ")
        champion = input("Enter champion name: ")
        result = input("Enter result (Victory/Defeat): ")
        kills = int(input("Enter number of kills: "))
        deaths = int(input("Enter number of deaths: "))
        assists = int(input("Enter number of assists: "))
        add_match(summoner_name, champion, result, kills, deaths, assists)
    
    elif choice == "3":
        summoner_name = input("Enter summoner name: ")
        profile = get_profile(summoner_name)
        print(profile)
    
    elif choice == "4":
        summoner_name = input("Enter summoner name: ")
        level = int(input("Enter level: "))
        server = input("Enter server: ")
        main_champion = input("Enter main champion: ")
        add_profile(summoner_name, level, server, main_champion)
    
    elif choice == "5":
        champion_name = input("Enter champion name: ")
        champion = get_champion(champion_name)
        print(champion)
    
    elif choice == "6":
        name = input("Enter champion name: ")
        champ_type = input("Enter champion type: ")
        difficulty = input("Enter champion difficulty: ")
        add_champion(name, champ_type, difficulty)
    
    elif choice == "7":
        break
    
    else:
        print("Invalid choice. Please try again.")
