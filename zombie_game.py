import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("植物大战僵尸简易版")

# 主循环标志
running = True

# 游戏主循环
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 填充背景颜色
    screen.fill((0, 128, 0))  # 绿色背景
    
    # 更新屏幕显示
    pygame.display.flip()

# 退出pygame
pygame.quit()
sys.exit()