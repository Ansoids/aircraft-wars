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
INTERVAL_OF_CREATE_BULLET= 300

# 自定义事件--创建小型敌机的ID
ID_OF_CREATE_SMALL_ENEMY = pygame.USEREVENT + 1
# 自定义事件--创建小型敌机的时间间隔
INTERVAL_OF_CREATE_SMALL_ENEMY= 2000

# 自定义事件--创建中型敌机的ID
ID_OF_CREATE_MID_ENEMY = pygame.USEREVENT + 2
# 自定义事件--创建中型敌机的时间间隔
INTERVAL_OF_CREATE_MID_ENEMY= 3600

# 自定义事件--创建大型敌机的ID
ID_OF_CREATE_BIG_ENEMY = pygame.USEREVENT + 3
# 自定义事件--创建大型敌机的时间间隔
INTERVAL_OF_CREATE_BIG_ENEMY= 18000

# 切换我方飞机图片频率
MY_PLANE_SWITCH_IMAGE_FREQUENCY = 3

# 切换我小型敌机爆炸图片频率
SMALL_PLANE_SWITCH_EXPLODE_IMAGE_FREQUENCY = 8

# 爆炸声音的音量
EXPLODE_SOUND_VOLUME = 0.8
