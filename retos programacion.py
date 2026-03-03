# -------------------------
# Clase Player
# -------------------------
class Player:
    def __init__(self, name, age, position, goals=0):
        self.name = name
        self.age = age
        self.position = position
        self.goals = goals

    def score(self):
        self.goals += 1
        print(f"{self.name} anotó un gol. Total goles: {self.goals}")

    def transfer(self, team_name):
        print(f"{self.name} fue transferido al equipo {team_name}.")


# -------------------------
# Clase Coach
# -------------------------
class Coach:
    def __init__(self, name, experience_years):
        self.name = name
        self.experience_years = experience_years

    def give_instructions(self):
        print(f"{self.name} dice: ¡Presionen alto y mantengan la posesión!")


# -------------------------
# Clase FootballTeam
# -------------------------
class FootballTeam:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.coach = None
        self.points = 0

    def add_player(self, player):
        self.players.append(player)

    def hire_coach(self, coach):
        self.coach = coach
        print(f"{coach.name} es ahora el entrenador de {self.name}")

    def show_players(self):
        print(f"\nJugadores de {self.name}:")
        for player in self.players:
            print(f"- {player.name} ({player.position})")

# EJECUCION

# Crear jugador
p1 = Player("Messi", 36, "Delantero")

# Crear entrenador
coach = Coach("Luis Enrique", 15)

# Crear equipo
team = FootballTeam("Dream FC")
team.add_player(p1)
team.hire_coach(coach)

# Probar métodos
p1.score()
coach.give_instructions()
team.show_players()