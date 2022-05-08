
import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode(size = (480, 700))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")
# 2.使用屏幕对象 调用blit方法
screen.blit(bg, (0,0))
# 3.调用update方法
# pygame.display.update()


# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200,500))

# 更新显示 - update 方法会把之前所有绘制的结果，一次性更新到屏幕窗口上
pygame.display.update()

# 英雄的初始化位置
hero_rect = pygame.Rect(200, 500, 102, 126)
# 游戏循环 ---> 意味着游戏的正式开始

# 创建时钟对象
clock = pygame.time.Clock()

while True:
    # 可以指定循环体体内部代码执行的频率
    clock.tick(1)

    # 修改英雄的位置
    hero_rect.y -= 20

    # 调用blit方法绘制图像
    # 先绘制背景图像，在绘制飞机图像
    screen.blit(bg, (0, 0))
    print(hero_rect.height)
    screen.blit(hero, hero_rect)


    # 调用update方法更新显示
    pygame.display.update()


pygame.quit()
