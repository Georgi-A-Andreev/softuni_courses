from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, 500)

    def win(self):
        self.advantage += 145
        self.wins += 1
