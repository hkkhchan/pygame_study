class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (133, 193, 255)
        self.ship_speed_factor = 1.5
        
        # bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
        
        # alien
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
