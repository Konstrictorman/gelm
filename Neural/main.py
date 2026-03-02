
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
from numpy.typing import NDArray
from sklearn.datasets import make_blobs

FArray = NDArray[np.float64]
IArray = NDArray[np.int64]

def sigmoid(x: FArray) -> FArray:
    return 1.0 / (1 + np.exp(-x))

def logistic(x:FArray, w:FArray) -> FArray:
    return sigmoid(x @ w.T)

def binary_crossentropy(y: IArray, y_hat: FArray) -> float:
    return - (y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat)).mean()

def gradient(x: FArray, y: IArray, w: FArray) -> FArray:
    y_hat = logistic(x, w)
    return (x * ((1-y) * y_hat - (1-y_hat)*y)).mean(axis=0, keepdims=True)

def init_weights(rnd: np.random.Generator) -> FArray:
    return rnd.standard_normal(size=(1,3))

#features, labels
x, y = make_blobs(
    n_samples=100, n_features=2,
    centers=2, cluster_std=0.5, random_state=0
    )
print(x)
x = np.concatenate([x, np.ones(shape=(x.shape[0], 1))], axis=1)
y = y.reshape(-1, 1)

# rng = np.random.default_rng(seed=0)
# w = init_weights(rng)
print(x)
# print(y)
# print(w)

# fig, ax = plt.subplots(figsize=(5, 5))
# ax.scatter(x[:,0], x[:,1], c=y)
# ax.scatter([1], [4], c="r")
# ax.set_xlabel('X')
# ax.set_ylabel('Y')

N_ITER = 1000
LEARNING_RATE = 0.1
loss = []
rng = np.random.default_rng(seed=1)
w = init_weights(rng)

for i in range(N_ITER):
    g = gradient(x, y, w)
    w = w - LEARNING_RATE * g
    loss.append(binary_crossentropy(y, logistic(x, w)))

fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(loss)
ax.set(xlabel="Iteración", ylabel="Pérdida")

x1 = np.linspace(-0.5, 4, 100)
x2 = np.linspace(-0.5, 6, 100)
X1, X2 = np.meshgrid(x1, x2)

x_grid = np.concatenate([X1.reshape(-1, 1), X2.reshape(-1, 1)], axis=1)
x_grid = np.concatenate([x_grid, np.ones(shape=(x_grid.shape[0], 1))], axis=1)
y_hat = logistic(x_grid, w)

fig, ax = plt.subplots()
cont = ax.contourf(X1, X2, y_hat.reshape(X1.shape), alpha=0.5, cmap="RdBu")
ax.scatter(x[:, 0], x[:, 1], c=y, cmap="RdBu")
ax.set(xlabel="x", ylabel="y")
fig.colorbar(cont)

plt.show()
