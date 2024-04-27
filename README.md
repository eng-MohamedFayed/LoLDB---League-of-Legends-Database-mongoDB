
# League of Legends Database Project

## Overview
This project provides a Python script to interact with a MongoDB database containing data related to League of Legends (LoL) match history, player profiles, and champion details. The project includes three collections: champions, matchHistory, and profiles. The `champions` collection stores information about LoL champions, including their name, type, and difficulty. The `matchHistory` collection records match data such as match ID, date, duration, result, summoner name, champion played, kills, deaths, and assists. The `profiles` collection contains player profiles with details like summoner name, level, server, and main champion.

## Requirements
- MongoDB installed and running on localhost.
- Python 3.x installed.

## Setup
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/League-of-Legends-DB.git
   ```
   
2. Navigate to the cloned directory:
   ```bash
   cd League-of-Legends-DB
   ```

3. Install the required Python packages:
   ```bash
   pip install pymongo
   ```

4. Import the JSON files into your MongoDB database:
   - Open a terminal or command prompt.
   - Use the `mongoimport` command to import each JSON file into their respective collections:
     ```bash
     mongoimport --db LOL --collection champions --file champions.json
     mongoimport --db LOL --collection matchHistory --file matchHistory.json
     mongoimport --db LOL --collection profiles --file profiles.json
     ```
   Replace `LOL` with your desired database name.

## Usage
1. Ensure that MongoDB is running.
2. Run the `LOL_DB.py` script with Python:
   ```bash
   python LOL_DB.py
   ```
3. Follow the prompts to interact with the database:
   - Get Match History
   - Add Match
   - Get Profile
   - Add Profile
   - Get Champion
   - Add Champion

## Example
```bash
1. Get Match History
2. Add Match
3. Get Profile
4. Add Profile
5. Get Champion
6. Add Champion
7. Exit
Enter your choice: 1
Enter summoner name: FrostQueen97
{'_id': ObjectId('65637a983179c288178e307d'), 'matchId': 1, 'date': datetime.datetime(2023, 11, 1, 0, 0), 'duration': '25:30', 'result': 'Victory', 'summonerName': 'FrostQueen97', 'champion': 'Ahri', 'kills': 10, 'deaths': 2, 'assists': 15, 'KillDeathPercent': 5.0}
{'_id': ObjectId('65637a983179c288178e3087'), 'matchId': 11, 'date': datetime.datetime(2023, 9, 28, 0, 0), 'duration': '27:20', 'result': 'Victory', 'summonerName': 'FrostQueen97', 'champion': 'Ahri', 'kills': 8, 'deaths': 1, 'assists': 10, 'KillDeathPercent': 8.0}
```

## Contribution
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to improve this project.

## License
This project is licensed under the [MIT License](LICENSE).
