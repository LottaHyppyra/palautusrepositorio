import requests
from player import Player
import datetime


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'], 
            player_dict['team'], 
            player_dict['goals'],
            player_dict['assists'],
            player_dict['nationality']
        )

        players.append(player)

    print(f"Players from FIN {datetime.datetime.now()}")

    for player in players:
        if player.nationality == "FIN":
            print(player)

if __name__ == "__main__":
    main()
