from cgitb import small
import sys
import pygame
from bullet import Bullet
from my_plane import MyPlane
from small_enemy import SmallEnemy
from mid_enemy import MidEnemy
from big_enemy import BigEnemy
import constans
from pygame.sprite import Group


class PlaneWar:
    """管理游戏的总体类"""
    def __init__(self) -> None:
        
        # 初始化pygame库
        pygame.init()

        # 创建窗口
        self._create_window()

        # 设置窗口
        self._set_window()

        # 创建一架我方飞机
        self.my_plane = MyPlane(self.window)

        # 创建管理画面精灵的分组
        self._create_groups()

        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()

        # 设置定时器
        self._set_timers()

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
    
    def _create_window(self):
        """创建窗口"""
        # 获得当前电脑屏幕的尺寸
        screen_width, screen_height = self.get_screen_size()
       
        # 根据当前电脑屏幕的尺寸计算窗口的尺寸
        window_width, window_height = screen_width * constans.SCALE_HORIZONTAL, screen_height * constans.SCALE_VERTICAL

        # 创建指定尺寸窗口
        self.window = pygame.display.set_mode((round(window_width), round(window_height)))

    def _set_window(self):
        """设置窗口"""
        #设置窗口标题
        pygame.display.set_caption("飞机大战")

        # 加载窗口图标
        window_icon = pygame.image.load("images/my_plane.png")

        # 设置窗口的图标
        pygame.display.set_icon(window_icon)

    def _create_groups(self):
        """创建管理精灵的分组"""

        # 创建一个管理所有子弹的分组
        self.bullet_group = Group()

        # 创建一个管理所有小型敌机的分组
        self.small_enemy_group = Group()

        # 创建一个管理所有中型敌机的分组
        self.mid_enemy_group = Group()

        # 创建一个管理所有大型敌机的分组
        self.big_enemy_group = Group()

        # 创建一个管理所有敌机的分组
        self.enemy_group = Group()

    def _set_timers(self):
        """设置定时器"""
        # 在事件队列中每隔一段按时间就生成一个自定义事件--创建子弹
        pygame.time.set_timer(constans.ID_OF_CREATE_BULLET, constans.INTERVAL_OF_CREATE_BULLET)

        # 在事件队列中每隔一段按时间就生成一个自定义事件--创建小型敌机
        pygame.time.set_timer(constans.ID_OF_CREATE_SMALL_ENEMY, constans.INTERVAL_OF_CREATE_SMALL_ENEMY)

        # 在事件队列中每隔一段按时间就生成一个自定义事件--创建中型敌机
        pygame.time.set_timer(constans.ID_OF_CREATE_MID_ENEMY, constans.INTERVAL_OF_CREATE_MID_ENEMY)
        
        # 在事件队列中每隔一段按时间就生成一个自定义事件--创建大型敌机
        pygame.time.set_timer(constans.ID_OF_CREATE_BIG_ENEMY, constans.INTERVAL_OF_CREATE_BIG_ENEMY)

    def run_game(self):
        while True:

            # 处理事件
            self._handle_events()

            # 设置窗口的背景色
            self.window.fill(pygame.Color("lightskyblue"))
            
            # 在窗口中绘制所有画面
            self._draw_elements()

            # 将内存中的窗口对象绘制到屏幕上以更新屏幕
            pygame.display.flip()

            # 在窗口中更新所有画面
            self._update_positions()

            # 删除窗口中所有不可见的元素
            self._delete_invisable_elements()

            # 设置while循环体在一秒内执行的次数（设置动画的最大帧率）
            self.clock.tick(constans.MAX_FRAMERATE)

    def _update_positions(self):
        """在窗口中更新所有画面元素"""

        # 更新我方飞机的位置    
        self.my_plane.update()

        # 更新所有子弹
        self.bullet_group.update()   

        # 更新所有小型敌机位置
        self.small_enemy_group.update()
 
        # 更新所有中型敌机位置
        self.mid_enemy_group.update()

        # 更新所有大型敌机位置
        self.big_enemy_group.update()

    def _delete_invisible_bullets(self):
        """删除窗口中所有不可见的子弹"""
        # 遍历子弹列表
        for bullet in self.bullet_group.sprites():        
            # 如果子弹在窗口中不见了
            if bullet.rect.bottom <= 0:
                # 从子弹列表中删除该颗子弹
                self.bullet_group.remove(bullet)

    def _delete_invisible_enemy(self):
        """删除窗口中所有不可见的敌机"""
        # 遍历所有敌机列表
        for enemy in self.enemy_group.sprites():        
            # 如果敌机在窗口中不见了
            if enemy.rect.top >= self.window.get_rect().height:
                # 将敌机从管理他的所有分组中删除
                enemy.kill()

    def _delete_invisable_elements(self):
        """"删除窗口中所有不可见的元素"""
        # 删除窗口中所有不可见子弹
        self._delete_invisible_bullets()

        # 删除窗口中所有不可见敌机
        self._delete_invisible_enemy()


    def _draw_elements(self):
        """在窗口中绘制所有画面元素"""

        # 在窗口中绘制我方飞机
        self.my_plane.draw()

        # 在窗口中绘制所有子弹
        for bullet in self.bullet_group.sprites():
            # 在窗口中绘制子弹
            bullet.draw()

        # 在窗口中绘制所有小型敌机
        for small_enemy in self.small_enemy_group.sprites():
            # 在窗口中绘制小型敌机
            small_enemy.draw()

        # 在窗口中绘制所有中型敌机
        for mid_enemy in self.mid_enemy_group.sprites():
            # 在窗口中绘制中型敌机
            mid_enemy.draw()

        # 在窗口中绘制所有大型敌机
        for big_enemy in self.big_enemy_group.sprites():
            # 在窗口中绘制大型敌机
            big_enemy.draw()
    
    def _handle_events(self):
        for event in pygame.event.get():
                # 判断事件是退出程序
                if event.type == pygame.QUIT:
                    # 卸载pygame库
                    pygame.quit()
                    # 退出程序
                    sys.exit()
                # 如果某个事件是用户按下了键盘上的某个键
                elif event.type == pygame.KEYDOWN:
                    
                    # 处理键盘按下事件
                    self._handle_keydown_events(event)

                # 如果某个事件是用户松开了键盘上的某个键
                elif event.type == pygame.KEYUP:

                    # 处理键盘松开事件
                    self._handle_keyup_events(event)

                # 如果某个事件是自定义事件 -- 创建子弹
                elif event.type == constans.ID_OF_CREATE_BULLET:
                    # 创建一颗子弹
                    bullet = Bullet(self.window, self.my_plane)
                    # 将创建的子弹添加到子弹分组中
                    self.bullet_group.add(bullet)

                # 如果某个事件是自定义事件 -- 创建小型敌机
                elif event.type == constans.ID_OF_CREATE_SMALL_ENEMY:
                    # 创建一架小型敌机
                    small_enemy = SmallEnemy(self.window)
                    # 将创建的小型敌机添加到敌机分组中
                    self.small_enemy_group.add(small_enemy)
                    # 将创建的小型敌机添加到管理所有敌机分组中
                    self.enemy_group.add(small_enemy)

                # 如果某个事件是自定义事件 -- 创建中型敌机
                elif event.type == constans.ID_OF_CREATE_MID_ENEMY:
                    # 创建一架中型敌机
                    mid_enemy = MidEnemy(self.window)
                    # 将创建的中型敌机添加到敌机分组中
                    self.mid_enemy_group.add(mid_enemy)
                    # 将创建的中型敌机添加到管理所有敌机分组中
                    self.enemy_group.add(mid_enemy)

                # 如果某个事件是自定义事件 -- 创建大型敌机
                elif event.type == constans.ID_OF_CREATE_BIG_ENEMY:
                    # 创建一架大型敌机
                    big_enemy = BigEnemy(self.window)
                    # 将创建的大型敌机添加到敌机分组中
                    self.big_enemy_group.add(big_enemy)
                    # 将创建的大型敌机添加到管理所有敌机分组中
                    self.enemy_group.add(big_enemy)
                    
    def _handle_keydown_events(self, event):
        """处理键盘按下事件"""

        # 如果按下的是上箭头
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            # 标记我方飞机向上移动
            self.my_plane.is_move_up = True

        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            # 标记我方飞机向下移动
            self.my_plane.is_move_down = True

        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            # 标记我方飞机向左移动
            self.my_plane.is_move_left = True

        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            # 标记我方飞机向右移动
            self.my_plane.is_move_right = True

        

    def _handle_keyup_events(self, event):
        """处理键盘松开事件"""

        # 如果松开的是上箭头
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            # 标记我方飞机不向上移动
            self.my_plane.is_move_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            # 标记我方飞机不向下移动
            self.my_plane.is_move_down = False

        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            # 标记我方飞机不向左移动
            self.my_plane.is_move_left = False

        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            # 标记我方飞机不向右移动
            self.my_plane.is_move_right = False


if __name__ == '__main__':

    PlaneWar().run_game()
