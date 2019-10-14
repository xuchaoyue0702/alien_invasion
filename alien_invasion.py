#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
from settings import Settings
from ship import Ship
from game_status import GameStatus
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建统计信息的实例
    status = GameStatus(ai_settings)

    # 创建飞船
    ship = Ship(ai_settings, screen)
    # alien = Alien(ai_settings, screen)
    # 创建一个存储子弹的编组
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, status, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == '__main__':
    run_game()
