from mycobot_controller.mycobot import MyCobot
import roboticstoolbox as rtb
import swift
import spatialmath as sm
import numpy as np


if __name__ == "__main__":  # pragma nocover

    env = swift.Swift()
    env.launch(realtime=True)
    robot = MyCobot()

    env.add(robot)

    print(robot)

    robot.q = (0.0, 0.785, 0.785, 1.57, 0.0, 0.0)

    env.step()

    Tep = robot.fkine(robot.q) * sm.SE3.Trans(0.1, 0.1, 0.1)
    arrived = False
    env.add(robot)

    dt = 0.005

    while not arrived:
        v, arrived = rtb.p_servo(robot.fkine(robot.q), Tep, 1)
        robot.qd = np.linalg.pinv(robot.jacobe(robot.q)) @ v
        env.step(dt)
