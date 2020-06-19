import os

import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding

from ssd_gym.envs.gathering import GatheringEnv


class HarverstEnv(GatheringEnv):
    """
    The Harverst Problem
    from "Multi-agent Reinforcement Learning in Sequential Social Dilemmas"
    by Leibo et al.
    Description:

    Observations: 

    Actions:

    Rewards: 

    Rendering:

    state space is represented by:

    """

    SPAWN_MAP = [
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
        '@ P   P      A    P AAAAA    P  A P  @',
        '@  P     A P AA    P    AAA    A  A  @',
        '@     A AAA  AAA    A    A AA AAAA   @',
        '@ A  AAA A    A  A AAA  A  A   A A   @',
        '@AAA  A A    A  AAA A  AAA        A P@',
        '@ A A  AAA  AAA  A A    A AA   AA AA @',
        '@  A A  AAA    A A  AAA    AAA  A    @',
        '@   AAA  A      AAA  A    AAAA       @',
        '@ P  A       A  A AAA    A  A      P @',
        '@A  AAA  A  A  AAA A    AAAA     P   @',
        '@    A A   AAA  A A      A AA   A  P @',
        '@     AAA   A A  AAA      AA   AAA P @',
        '@ A    A     AAA  A  P          A    @',
        '@       P     A         P  P P     P @',
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    ]

    ORI_MAP = [
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@                                    @',
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    ]

    def __init__(self, n_agents):
        super(HarverstEnv, self).__init__()
        self.observation_space = spaces.Box(
            low=0, high=3, shape=(16, 38), dtype=np.uint8)
        self.MAP = self.ORI_MAP.copy()
        self.n_agents = n_agents
        self.agents_points = [(0, 0) for _ in range(n_agents)]
        self.spawn_points_agents = self.get_spawn(match='P')
        self.spawn_points_apples = self.get_spawn(match='A')

    def step(self, action):
        raise NotImplementedError

    def reset(self):
        self.MAP = self.ORI_MAP.copy()
        for i in range(self.n_agents):
            row = np.random.choice(list(self.spawn_points_agents.keys()))
            col = np.random.choice(self.spawn_points_agents[row])
            while self.MAP[row][col] == 'P':
                row = np.random.choice(list(self.spawn_points_agents.keys()))
                col = np.random.choice(self.spawn_points_agents[row])
            self.MAP[row][col] = 'P'
            self.agents_points[i] = (row, col)
        # Implement apples

    def render(self, mode='human', close=False):
        os.system('clear')
        for row in self.MAP:
            print(row)

    def get_spawn(self, match):
        possible_points = {i: list() for i in range(1, len(self.SPAWN_MAP)-1)}
        for i in range(1, len(self.SPAWN_MAP) - 1):
            for j in range(1, len(self.SPAWN_MAP[0]) - 1):
                if self.SPAWN_MAP[i][j] == match:
                    possible_points[i].append(j)
        return possible_points
