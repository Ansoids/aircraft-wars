import sys
import pygame
import datetime

class PlaneWar:
    """管理游戏的总体类"""
    def __init__(self) -> None:
        
        # 初始化pygame库
        pygame.init()
        # 创建指定尺寸窗口
        self.pos_y = 774
        self.window = pygame.display.set_mode((700, 900))

        pygame.display.set_caption("飞机大战")

        self.my_plane = pygame.image.load("images/my_plane.png")
        
        self.clock = pygame.time.Clock()
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                # 判断事件是退出程序
                if event.type == pygame.QUIT:
                    # 卸载pygame库
                    pygame.quit()
                    # 退出程序
                    sys.exit()

            self.window.fill(pygame.Color("lightskyblue"))
            # 在指定坐标位置加载图片
            self.window.blit(self.my_plane, (299, self.pos_y))
            # 将内存中的窗口对象绘制到屏幕上以更新屏幕
            pygame.display.flip()
                
            self.pos_y -= 20

            # 设置while循环体在一秒内执行的次数（设置动画的最大帧率）
            self.clock.tick(30)

if __name__ == '__main__':

    PlaneWar().run_game()
