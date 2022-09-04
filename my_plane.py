"""我方飞机"""
import pygame

class MyPlane:
    """我方飞机类"""

    def __init__(self, window) -> None:
        """初始化我方飞机"""

        # 获得窗口对象
        self.window = window

        #加载我方飞机图片
        self.image = pygame.image.load("images/my_plane.png")

        # 获得我方飞机矩形
        self.rect = self.image.get_rect()

        # 获得窗口矩形
        self.window_rect = self.window.get_rect()

        # 设置我方飞机的矩形的初始位置为：窗口的底部居中位置
        self.rect.midbottom = self.window_rect.midbottom
        
    def update(self):
        """更新我方飞机位置"""

        #减少我方飞机的Y坐标向上移动
        self.rect.top -= 20
       
    def draw(self):
        """在窗口中绘制我方飞机"""

        # 在指定坐标位置加载图片
        self.window.blit(self.image, self.rect)
        