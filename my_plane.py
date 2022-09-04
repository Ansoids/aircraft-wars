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

        # 标记我方飞机不向上移动
        self.is_move_up = False
        # 标记我方飞机不向下移动
        self.is_move_down = False
        # 标记我方飞机不向左移动
        self.is_move_left = False
        # 标记我方飞机不向右移动
        self.is_move_right = False
        
    def update(self):
        """更新我方飞机位置"""

        if self.is_move_up and self.rect.top - 20 > 0:           
            # 减少我方飞机的矩形的属性top以向上移动
            self.rect.top -= 20 
        if self.is_move_down and self.rect.bottom + 20 < self.window_rect.height:         
            # 增大我方飞机的矩形的属性bottom以向下移动
            self.rect.bottom += 20
        if self.is_move_left and self.rect.left - 20 > 0:          
            # 减少我方飞机的矩形的属性left以向左移动
            self.rect.left -= 20
        if self.is_move_right and self.rect.right + 20 < self.window_rect.width:           
            # 增大我方飞机的矩形的属性right以向右移动
            self.rect.right += 20
       
    def draw(self):
        """在窗口中绘制我方飞机"""

        # 在指定坐标位置加载图片
        self.window.blit(self.image, self.rect)
        