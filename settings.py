#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Settings:
    # 存储所有设置
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1为向右移，-1为向左移
        self.fleet_direction = 1
