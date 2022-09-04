import sys
import pygame
from my_plane import MyPlane


class PlaneWar:
    """管理游戏的总体类"""
    def __init__(self) -> None:
        
        # 初始化pygame库
        pygame.init()

        # 获得当前电脑屏幕的尺寸
        screen_width, screen_height = self.get_screen_size()
       
        # 根据当前电脑屏幕的尺寸计算窗口的尺寸
        window_width, window_height = screen_width * (2 / 5), screen_height * (4 / 5)


        # 创建指定尺寸窗口
        self.window = pygame.display.set_mode((round(window_width), round(window_height)))

        # 设置窗口
        self._set_window()

        # 创建一架我方飞机
        self.my_plane = MyPlane(self.window)

        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()

    def get_screen_size(self):
        """获得当前电脑屏幕的尺寸"""
        # 创建一个视频显示对象
        info = pygame.display.Info()

        # 获得当前电脑屏幕高度
        screen_height = info.current_h

        # 获得当前电脑屏幕宽度
        screen_weight = info.current_w

        # 返回当前电脑屏幕的宽度及高度
        return screen_weight, screen_height

    def _set_window(self):
        """设置窗口"""
        #设置窗口标题
        pygame.display.set_caption("飞机大战")

        # 加载窗口图标
        window_icon = pygame.image.load("images/my_plane.png")

        # 设置窗口的图标
        pygame.display.set_icon(window_icon)
        
    def run_game(self):
        while True:

            # 处理事件
            self._handle_events()

            # 设置窗口的背景色
            self.window.fill(pygame.Color("lightskyblue"))
            
            # 在窗口中绘制我方飞机
            self.my_plane.draw()

            # 将内存中的窗口对象绘制到屏幕上以更新屏幕
            pygame.display.flip()

            # 更新我方飞机的位置    
            self.my_plane.update()

            # 设置while循环体在一秒内执行的次数（设置动画的最大帧率）
            self.clock.tick(30)
    
    def _handle_events(self):
        for event in pygame.event.get():
                # 判断事件是退出程序
                if event.type == pygame.QUIT:
                    # 卸载pygame库
                    pygame.quit()
                    # 退出程序
                    sys.exit()

if __name__ == '__main__':

    PlaneWar().run_game()
