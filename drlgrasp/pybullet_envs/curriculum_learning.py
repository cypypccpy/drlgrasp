import pybullet as p
import pybullet_data
import gym

from gym import spaces
from gym.utils import seeding
import numpy as np
from math import sqrt, tanh
import random
import time
import math
import cv2
import torch
import os

class curriculum_learning():
    def __init__(self) -> None:
        self.grasp_scale = 2.0
        self.model_scale = 2.0

    def set_grasp_scale(self, epoch) -> None:
        if epoch < 1000:
            factor1 = min(0.5 * sqrt(epoch / 150), 1.0)
            self.grasp_scale = 2 - factor1 * 0.5
            self.model_scale = 2 - factor1 * 0.5
        
        if 10000 > epoch > 1000:
            factor2 = min(0.5 * sqrt(epoch / 2500), 1.0)
            self.grasp_scale = 1.5 - factor2 * 0.5
            self.model_scale = 1.5 - factor2 * 0.5

        if epoch > 10000:
            self.grasp_scale = 1.0
            self.model_scale = 1.0
    
    def get_grasp_scale(self) -> float:
        return self.grasp_scale * 1.5
        
    def get_model_scale(self) -> float:
        return self.model_scale