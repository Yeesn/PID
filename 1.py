import time


class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.last_error = 0
        self.integral = 0

    def update(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.last_error) / dt
        output = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)
        self.last_error = error
        return output


# 初始化PID控制器
pid_controller = PIDController(Kp=1.0, Ki=0.1, Kd=0.05)

# 设定目标速度
target_speed = 10.0

# 模拟小车运动
current_speed = 0.0
current_time = time.time()

while True:
    # 计算时间间隔
    dt = time.time() - current_time

    # 计算速度误差
    speed_error = target_speed - current_speed

    # 使用PID控制器计算输出
    output = pid_controller.update(speed_error, dt)

    # 更新小车速度
    current_speed += output

    # 输出结果
    print("Current Speed: {:.2f}".format(current_speed))

    # 更新时间戳
    current_time = time.time()
