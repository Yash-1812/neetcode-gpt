import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        max_val = max(z)
        a = np.exp(z - max_val)
        b = np.sum(a)
        return np.round(a / b , 4)
