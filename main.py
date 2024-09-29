import pygame
import sys


WHITE = (255, 255, 255)

# 初始化Pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置标题
pygame.display.set_caption('张学良下飞机')



# 设置时钟
clock = pygame.time.Clock()

# 加载图像
plane_image = pygame.image.load('plane.png')
general_image = pygame.image.load('zxl.png')
soldier1_image = pygame.image.load('soldier1.png')
soldier2_image = pygame.image.load('soldier2.png')

plane_image = pygame.transform.scale(plane_image, (200, 100))
general_image = pygame.transform.scale(general_image, (50, 50))
soldier1_image = pygame.transform.scale(soldier1_image, (50, 50))
soldier2_image = pygame.transform.scale(soldier2_image, (50, 50))

# 设置初始位置
plane_rect = plane_image.get_rect()
plane_rect.x = 0
plane_rect.y = (screen_height - plane_rect.height) // 2

general_rect = general_image.get_rect()
general_rect.x = screen_width // 2 - general_rect.width // 2
general_rect.y = screen_height // 2

soldier1_rect = soldier1_image.get_rect()
soldier1_rect.x = general_rect.x - soldier1_rect.width - 20
soldier1_rect.y = general_rect.y + general_rect.height + 20

soldier2_rect = soldier2_image.get_rect()
soldier2_rect.x = general_rect.x + general_rect.width + 20
soldier2_rect.y = general_rect.y + general_rect.height + 20

# 移动标志
plane_moving = True
general_walking = False

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 飞机移动
    if plane_moving:
        plane_rect.x += 2
        if plane_rect.x > screen_width // 2 - plane_rect.width // 2:
            plane_moving = False
            general_walking = True

    # 将军和士兵行走
    if general_walking:
        general_rect.y += 2
        if general_rect.y > soldier1_rect.y:
            soldier1_rect.y += 2
            soldier2_rect.y += 2

        if general_rect.y > screen_height - general_rect.height:
            pygame.quit()
            sys.exit()

    # 清空屏幕
    screen.fill(WHITE)

    # 绘制飞机
    screen.blit(plane_image, plane_rect)
    screen.blit(soldier1_image, soldier1_rect)
    screen.blit(soldier2_image, soldier2_rect)

    # 只有当飞机停止移动时，才绘制将军和士兵
    if not plane_moving:
        screen.blit(general_image, general_rect)

    # 更新屏幕
    pygame.display.flip()

    # 控制游戏帧率
    clock.tick(30)