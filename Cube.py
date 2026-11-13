import numpy as np
from mvt import *

class Cube:
    def __init__(self, state:np.ndarray=None):
        if state is None:
            self.state = np.zeros(54, dtype=np.uint8)
        else:
            self.state = state

    def move(self, mvt: np.ndarray):
        self.state = self.state[mvt]