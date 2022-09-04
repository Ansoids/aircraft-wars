"""子弹"""
import pygame

class Bullet:
    """子弹类"""

    def __init__(self, window, my_plane) -> None:
        """初始化子弹"""

        # 获得窗口对象
        self.window = window

        #加载子弹图片
        self.image = pygame.image.load("images/bullet.png")

        # 获得子弹矩形
        self.rect = self.image.get_rect()

        # 获得我方飞机矩形
        self.my_plane_rect = my_plane.rect

        # 设置子弹的矩形的初始位置为：我方飞机的顶部居中位置
        self.rect.midtop = self.my_plane_rect.midtop

       # 子弹每次移动的偏移量
        self.offset = 50
        
    def update(self):
        """更新子弹位置"""
        # 减少子弹的矩形的属性top以向上移动
        self.rect.top -= self.offset 
       
    def draw(self):
        """在窗口中绘制子弹"""

        # 在指定坐标位置加载图片
        self.window.blit(self.image, self.rect)
        