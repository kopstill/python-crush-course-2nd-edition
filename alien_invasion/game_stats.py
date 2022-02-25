class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.ships_left = self.settings.ship_limit
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = self.read_high_score()
        self.last_high_score = int(self.high_score)

    def read_high_score(self):
        try:
            with open('high_score.txt') as f:
                high_score = f.read()
                return int(high_score)
        except FileNotFoundError:
            return 0

    def write_high_score(self):
        if self.score > self.last_high_score:
            with open("high_score.txt", 'w') as f:
                f.write(str(round(self.score, -1)))

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def level_up(self):
        self.level += 1

    def reset_level(self):
        self.level = 1
