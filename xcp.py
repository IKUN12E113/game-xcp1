import pygame
import random

# 初始化pygame
pygame.init()

# 设置窗口大小
WIDTH, HEIGHT = 1300, 700

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("打许超萍游戏")

# 加载背景、地鼠和锤子图片
background_image = pygame.image.load(r'image\background_image.jpg')
mouse_image = pygame.image.load(r'image\mouse_image.png')
hammer_image = pygame.image.load(r'image\hammer.png')
mouse_rect = mouse_image.get_rect()

# 设置字体
font = pygame.font.Font(None, 36)
score_text = font.render("Score: 0", True, (0, 0, 0))

# 游戏变量
score = 0
running = True

# 游戏主循环
while running:
    # 绘制背景
    screen.blit(background_image, (0, 0))

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_rect.collidepoint(mouse_x, mouse_y):
                score += 1
                # 重新设置地鼠的位置
                mouse_rect.topleft = (random.randint(0, WIDTH - mouse_rect.width), random.randint(0, HEIGHT - mouse_rect.height))
                # 更新分数显示
                score_text = font.render("Score: " + str(score), True, (0, 0, 0))
                # 显示挥锤特效
                hammer_rect = hammer_image.get_rect(center=(mouse_x, mouse_y))
                screen.blit(hammer_image, hammer_rect)
                pygame.display.flip()  # 更新屏幕以显示锤子
                pygame.time.wait(100)  # 等待一段时间，以显示挥锤效果

    # 绘制地鼠
    screen.blit(mouse_image, mouse_rect)

    # 显示分数
    screen.blit(score_text, (10, 10))

    # 更新屏幕
    pygame.display.flip()

# 退出游戏
pygame.quit()
