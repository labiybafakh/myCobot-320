#!/usr/bin/env python

import os 
import numpy as np
from roboticstoolbox.robot.Robot import Robot
from math import pi
import swift
import spatialmath as sm
import numpy as np
import roboticstoolbox as rtb


class MyCobot(Robot):

    def __init__(self):

        links, name, urdf_string, urdf_filepath = self.URDF_read(os.path.join(os.path.dirname(__file__), "URDF/new_mycobot_pro_320.urdf"))

        super().__init__(
            links,
            name=name,
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )

        self.manufacturer = "myCobot"

        # # zero angles, upper arm pointing up, lower arm straight ahead
        # self.addconfiguration("qz", np.array([0, 0, 0, 0]))

        # # reference pose robot pointing upwards
        # self.addconfiguration("up", np.array([0.0000, 0.0000, 1.5707, 0.0000]))


if __name__ == "__main__":  # pragma nocover

    # env = swift.Swift()
    # env.launch(realtime=True)
    robot = MyCobot()

    print(robot)

    # robot.q = robot.qr

    # Tep = robot.fkine(robot.q) * sm.SE3.Trans(0.2, 0.2, 0.45)
    # arrived = False
    # env.add(robot)

    # dt = 0.05

    # while not arrived:

    #     v, arrived = rtb.p_servo(robot.fkine(robot.q), Tep, 1)
    #     robot.qd = np.linalg.pinv(robot.jacobe(robot.q)) @ v
    #     env.step(dt)
