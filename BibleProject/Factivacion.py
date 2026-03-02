import numpy as np
import matplotlib.pyplot as plt

from numpy.typing import NDArray

plt.style.use("ggplot")


#Heaviside
def heaviside(x: NDArray[np.float64]) -> NDArray[np.int32]:
    return (x >0).astype(np.int32)

#Sigmoid
def sigmoid(x: NDArray[np.float64]) -> NDArray[np.float32]:
    return 1.0/ (1+np.exp(-x))

x = np.linspace(-10, 10, 100)
fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(x, heaviside(x), color='red', label='Heaviside')
ax.plot(x, sigmoid(x), color='blue', label='Sigmoid')
ax.legend()
ax.set(xlabel='$x$', ylabel='$f(x)$')




plt.show()
