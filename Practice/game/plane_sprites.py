
import pygame
import random

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREAT_ENEMY_EVENT = pygame.USEREVENT
# 创建子弹的定时器常量---英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed

class Background(GameSprite):

    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 2.判断是否是交替图像，如果是，则需要设置初始化位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的方法实现
        super().update()
        # 2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):

    def __init__(self):
        # 1.调用父类方法创建敌机精灵
        super().__init__("./images/enemy1.png")

        # 2.指定敌机的初始速度
        self.speed = random.randint(1,3)
        # 3.指定敌机的初始随机位置
        max_x = SCREEN_RECT.width-self.rect.width
        self.rect.x = random.randint(0, max_x)

        self.rect.bottom = 0
        # self.rect.y = -self.rect.height

    def update(self):
        # 1.更新父类的方法实现，保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除...")
            # kill方法可以将精灵从所有精灵组中移出，精灵就会被自动销毁
            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass

class Hero(GameSprite):

    """英雄精灵"""
    def __init__(self):
        # 调用父类方法，设置image&speed
        super().__init__("./images/me1.png", 0)

        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-120

        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()
    def update(self):
        # 英雄在水平方向移动
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width

    def fire(self):
        # print("发射子弹...")
        for i in range(0,3):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3.将子弹精灵添加到精灵组
            self.bullets.add(bullet)



class Bullet(GameSprite):

    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./images/bullet1.png", -2)

    def update(self):

        # 调用父类方法，子弹向上移动，所以初始速度设置为负值
        super().update()
        # 当子弹飞出上方屏幕后，就将子弹销毁
        if self.rect.bottom < 0:
            self.kill()

        pass

    def __del__(self):
        # print("子弹被销毁")
        pass

