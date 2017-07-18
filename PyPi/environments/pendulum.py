import gym
import numpy as np

from PyPi.environments import Environment
from PyPi.utils import spaces


class Pendulum(Environment):
    def __init__(self):
        self.__name__ = 'Pendulum-v0'

        # MPD creation
        self.env = gym.make(self.__name__)

        # MDP spaces
        high = np.array([np.pi, self.env.max_speed])
        self.action_space = self.env.action_space
        self.observation_space = self.env.observation_space

        # MDP parameters
        self.horizon = 100
        self.gamma = 0.95

        super(Pendulum, self).__init__()

    def reset(self, state=None):
        if state is None:
            self.env.reset()
        else:
            self.env.state = state

        return self.get_state()

    def step(self, action):
        _, reward, absorbing, info = self.env.step(action)

        return self.get_state(), reward, absorbing, info

    def render(self, mode='human', close=False):
        self.env.render(mode=mode, close=close)