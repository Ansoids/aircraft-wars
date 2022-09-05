"""所有常量"""

import pygame

# 在水平方向上， 窗口尺寸占电脑屏幕尺寸的比例
SCALE_HORIZONTAL = 2 / 5
# # 在竖直方向上， 窗口尺寸占电脑屏幕尺寸的比例
SCALE_VERTICAL = 4 / 5
# 动画的最大帧率
MAX_FRAMERATE = 30
# 自定义事件--创建子弹的ID
ID_OF_CREATE_BULLET = pygame.USEREVENT
# 自定义事件--创建子弹的时间间隔
INTERVAL_OF_CREATE_BULLET= 500

# 自定义事件--创建小型敌机的ID
ID_OF_CREATE_SMALL_ENEMY = pygame.USEREVENT + 1
# 自定义事件--创建小型敌机的时间间隔
INTERVAL_OF_CREATE_SMALL_ENEMY= 2000