
import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode(size = (480, 700))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")
# 2.使用屏幕对象 调用blit方法
screen.blit(bg,(0,0))
# 3.调用update方法
pygame.display.update()

while True:
    pass

pygame.quit()
