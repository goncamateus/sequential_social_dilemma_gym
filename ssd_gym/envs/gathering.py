import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding


class GatheringEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    MAP = []
    def __init__(self):

        self.viewer = None

        self.action_space = spaces.Discrete(9)
    
    def step(self, action_n):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def render(self, mode='human', close=False):
        raise NotImplementedError
