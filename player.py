from draw_utils import Color

player_names = ["A", "B", "C", "D", "E", "F"]

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class PlayerManager:
    def __init__(self, number_of_players):
        self.players = []
        names = ["player1", "player2"]
        for i in range(number_of_players):
            #name = input(f"player {i+1} name\n")
            self.players.append(Player(names[i], Color.yellow))
