

class Pong:

    def __init__(self):

        self.width = 640
        self.height = 480

        self.ball_pos = [0, 0]
        self.ball_vel = [100, 0]

        self.paddle_pos = [0, 0]
        self.paddle_vel = [0, 0]

    def step(self, inputs):

        dt = 0.0166

        self.ball_pos[0] += self.ball.vel[0] * dt
        self.ball_pos[1] += self.ball.vel[1] * dt

        self.paddle_pos[0] += self.paddle.vel[0] * dt
        self.paddle_pos[1] += self.paddle.vel[1] * dt

        self.paddle_vel[0] += inputs[0] * dt
        self.paddle_vel[1] += inputs[1] * dt
