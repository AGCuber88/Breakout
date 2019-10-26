class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 120)
        self.bg_color_transparent = (255, 255, 120, 255)

        self.ball_width = 20
        self.ball_height = 20
        #self.ball_color = (255, 10, 0)
        self.ball_color = (255, 255, 255)
        self.ball_speed_factor_y = 3
        self.ball_speed_factor_x = 3

        self.paddle_width = 150
        self.paddle_height = 15
        #self.paddle_color = (0, 0, 0)
        self.paddle_color = (0, 255, 0)
        self.paddle_speed_factor = 3

        self.block_width = 160
        self.block_height = 30
        self.block_color = (0, 128, 255)
        self.block_points = 50



