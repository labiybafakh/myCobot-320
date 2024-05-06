#!/usr/bin/env python

import os
import numpy as np
from roboticstoolbox.robot.Robot import Robot
from math import pi

class MyCobot(Robot):

    def __init__(self):
        links, name, urdf_string, urdf_filepath = self.URDF_read(
            file_path=os.path.join(
                os.path.dirname(__file__), "URDF/new_mycobot_pro_320.urdf"
            ),
            tld=os.path.join(os.path.dirname(__file__), "URDF"),
        )

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

