class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, name, position, number, age, nationality):
        player = {
            "name": name,
            "position": position,
            "number": number,
            "age": age,
            "nationality": nationality
        }
        self.players.append(player)
        print(f"{name} successfully added!")

    def remove_player(self, number):
        for player in self.players:
            if player["number"] == number:
                self.players.remove(player)
                print("Player removed successfully!")
                return
        print("Player not found!")

    def update_player(self, number, key, value):
        for player in self.players:
            if player["number"] == number:
                player[key] = value
                print("Player information updated!")
                return
        print("Player not found!")

    def show_team_info(self):
        print(f"Team Name: {self.team_name}")
        print(f"Coach: {self.coach}")
        print("Players:")
        for player in self.players:
            print(player)

    def show_player_info(self, number):
        for player in self.players:
            if player["number"] == number:
                print(player)
                return
        print("Player not found!")


team = FootballTeam("Barcelona", "Luis Enrique")

team.add_player("Lionel Messi", "Forward", 10, 28, "Argentina")
team.add_player("Neymar Jr", "Forward", 11, 23, "Brazil")
team.add_player("Luis Suarez", "Striker", 9, 28, "Uruguay")

team.show_team_info()

team.update_player(10, "goals", 2)
team.update_player(10, "assists", 1)

team.show_player_info(10)

team.remove_player(11)

team.show_team_info()
