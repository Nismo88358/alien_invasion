import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")
    # Создание экземпляров GameStats и Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Создание коробля
    ship = Ship(ai_settings, screen)
    # Создание групп пуль и групп пришельцев.
    bullets = Group()
    aliens = Group()
    # Создание пришельца.
    alien = Alien(ai_settings, screen)
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
            # Удаление пуль, вышедших за край экрана.
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens, bullets, play_button)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()
