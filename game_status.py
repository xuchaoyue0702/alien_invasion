#!/usr/bin/env python
# -*- coding:utf-8 -*-


class GameStatus:
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_status()

    def reset_status(self):
        """初始化游戏运行期间可能变化的信息"""
        self.ships_left = self.ai_settings.ship_limit
