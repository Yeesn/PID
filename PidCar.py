import time
import pygame as pg
import math
from pygame.locals import *


pg.init()
size = width, height = 800, 600  # 屏幕大小
screen = pg.display.set_mode(size)
pg.display.set_caption('car')

x, y = 430, 110  # 小车初始位置
speed = 0.3  # 速度标量
velocity = [0, 0]  # 速度矢量
angle = 0  # 初始角度

kp = 0.5
kd = 0.1
last_error = 0

path = [(x, y)]  # 轨迹

run = True  # 运行标志
pause = False  # 暂停标志


def color_binary(colors):
    # 颜色二值化 RGBA>>>0/1
    rval = []
    for color in colors:
        # 白色
        if color == (255, 255, 255, 255):
            rval.append(0)
        # 黑色
        elif color == (0, 0, 0, 255):
            rval.append(1)
    # print(rval)
    return rval

def get_gs_sensor_value(x, y, angle):
    # 获取灰度传感器值 并绘制传感器圆
    step1 = 11
    step2 = 19
    step3 = 15

    # 两坐标轴方向
    angle1 = math.pi * (angle + 90) / 180
    angle2 = math.pi * (angle) / 180

    x0 = x + step2 * math.cos(angle1) + step3 * math.cos(angle2)
    y0 = y - step2 * math.sin(angle1) - step3 * math.sin(angle2)
    pg.draw.circle(screen, (255, 0, 0), (int(x0), int(y0)), 3, 1)  # 绘制0号灰度

    x1 = x + step1 * math.cos(angle1) + step3 * math.cos(angle2)
    y1 = y - step1 * math.sin(angle1) - step3 * math.sin(angle2)
    pg.draw.circle(screen, (255, 0, 0), (int(x1), int(y1)), 3, 1)  # 绘制1号灰度

    x2, y2 = x + step3 * math.cos(angle2), y - step3 * math.sin(angle2)
    pg.draw.circle(screen, (255, 0, 0), (int(x2), int(y2)), 3, 1)  # 绘制2号（中间）灰度

    x3 = x - step1 * math.cos(angle1) + step3 * math.cos(angle2)
    y3 = y + step1 * math.sin(angle1) - step3 * math.sin(angle2)
    x4 = x - step2 * math.cos(angle1) + step3 * math.cos(angle2)
    y4 = y + step2 * math.sin(angle1) - step3 * math.sin(angle2)
    pg.draw.circle(screen, (255, 0, 0), (int(x3), int(y3)), 3, 1)  # 绘制3号灰度
    pg.draw.circle(screen, (255, 0, 0), (int(x4), int(y4)), 3, 1)  # 绘制4号灰度

    # 灰度传感器对应的像素值
    try:
        g0 = screen.get_at((int(x0), int(y0)))
        g1 = screen.get_at((int(x1), int(y1)))
        g2 = screen.get_at((int(x2), int(y2)))
        g3 = screen.get_at((int(x3), int(y3)))
        g4 = screen.get_at((int(x4), int(y4)))
    except:
        g0, g1, g2, g3, g4 = (255, 255, 255, 255, 255)

    x5 = x + 100 * math.cos(angle2)
    y5 = y - 100 * math.sin(angle2)
    pg.draw.line(screen, (255, 0, 0), (x, y), (x5, y5), 1)  # 绘制方向指示线

    return color_binary([g0, g1, g2, g3, g4])

def pid_angle(gs):
    # pid 调速
    # :gs:灰度传感器数组
    global angle
    global last_error
    gs_black = 0  # 检测到黑色的灰度传感器数量
    sum_ = 0
    for i in range(len(gs)):
        if gs[i] == 1:
            gs_black += 1
            sum_ += i

    if gs_black != 0:
        sum_ = sum_ * 10 / gs_black - 20  # 计算误差

    pid_p_out = kp * sum_  # p
    ed = sum_ - last_error  # 本次误差
    last_error = sum_  # 更新上次误差
    pid_d_out = kd * ed  # d

    pid_out = pid_p_out + pid_d_out
    angle = angle - pid_out

    if angle <= -180:
        angle = 180


def set_velocity(angle):
    global speed, velocity, x, y
    angle = math.pi * (-angle) / 180
    velocity[0] = speed * math.cos(angle)
    velocity[1] = speed * math.sin(angle)
    x += velocity[0]
    y += velocity[1]

    # 边界检测
    if x <= 0:
        x = 0
        speed = 0
    if x >= width:
        x = width
        speed = 0
    if y <= 0:
        y = 0
        speed = 0
    if y >= height:
        y = height
        speed = 0

def main_loop():
    global run, pause, angle, x, y
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:  # P键暂停
                    pause = not pause
                if event.key == pg.K_r:  # R键重新开始
                    x, y = 555, 206
                    angle = 0
                    path.clear()
                    path.append((x, y))

        if pause:
            continue

        set_velocity(angle)  # 设置速度

        # 绘图
        screen.fill((255, 255, 255))  # 绘制白色背景
        # pg.draw.ellipse(screen, (0, 0, 0), Rect((100, 100), (650, 300)), 20)  # 绘制跑道
        pg.draw.rect(screen, (0, 0, 0), Rect((100, 100), (650, 300)), 20)
        pg.draw.line(screen, (0, 0, 0), (425, 100), (425, 400), 20)
        pg.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 10, 1)  # 绘制圆代替小车
        # gs = [0, 0, 1, 0, 0]
        gs = get_gs_sensor_value(x, y, angle)  # 获取灰度传感器值
        pid_angle(gs)  # pid调速
        pg.display.flip()  # 重新绘制窗口
    pg.quit()
    return


main_loop()
