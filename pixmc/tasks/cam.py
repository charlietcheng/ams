import numpy as np
import isaacgym
from isaacgym import gymapi

class Camera:
    def __init__(self, look_from, look_at, env_ptr, width, height) -> None:
        self.cam_prop = gymapi.CameraProperties()
        self.height = 480
        self.width = 640
        self.env_ptr = env_ptr
        self.look_from = look_from
        self.look_at = look_at
        self.cam_prop.width = width
        self.cam_prop.height = height



        