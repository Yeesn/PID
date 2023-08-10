import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Keyboard events")

clock = pygame.time.Clock()

x, y = 0, 0
dx, dy = 0, 0

while True:
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # 根据按键状态改变坐标
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -5
            elif event.key == pygame.K_RIGHT:
                dx = 5
            elif event.key == pygame.K_UP:
                dy = -5
            elif event.key == pygame.K_DOWN:
                dy = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx = 0
            elif event.key == pygame.K_RIGHT:
                dx = 0
            elif event.key == pygame.K_UP:
                dy = 0
            elif event.key == pygame.K_DOWN:
                dy = 0

    # 移动矩形
    x += dx
    y += dy

    # 显示矩形
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 50, 50))
    pygame.display.update()

    # 控制游戏帧率
    clock.tick(60)