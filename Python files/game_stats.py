
class GameStats:

    def __init__(self, settings):
        self.settings = settings
        self.game_active = False
        self.score = 0

        with open("Highscore.txt") as file:
            self.high_score = file.read()

        self.high_score = int(self.high_score)
        self.lives_left = 2
        self.level = 1
        self.settings.block_points = 50


    def reset_stats(self):
        self.level = 1
        self.score = 0
        self.lives_left = 2
        self.settings.block_points = 50
