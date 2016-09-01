<<<<<<< HEAD
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
run_game()
=======
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
run_game()
>>>>>>> e23426df7249af5bcb36ceff96f1cd9b715a9f39
