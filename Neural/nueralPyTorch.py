import torch

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


def sigmoid(u: torch.Tensor) -> torch.Tensor:
    return 1.0 / (1 + torch.exp(-u))

def logistic(x: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
    return sigmoid(x @ w.T)

def binary_crossentropy(y: torch.Tensor, y_hat: torch.Tensor) -> torch.Tensor:
    return -(y * torch.log(y_hat) + (1 - y) * torch.log(1 - y_hat)).mean()

def init_weights() -> torch.Tensor:
    return torch.randn(size=(1, 3))


x, y = make_blobs(
    n_samples=1000, n_features=2,
    centers=2, cluster_std=0.5, random_state=0
    )
x = np.concatenate([x, np.ones(shape=(x.shape[0], 1))], axis=1)
y = y.reshape(-1, 1)

x_torch = torch.tensor(x, dtype=torch.float32)
y_torch = torch.tensor(y, dtype=torch.float32)

N_ITER = 100
LEARNING_RATE = 1
loss = []
w = init_weights()
for i in range(N_ITER):
    w = w.detach().clone().requires_grad_(True)
    y_hat = logistic(x_torch, w)
    cur_loss = binary_crossentropy(y_torch, y_hat)
    cur_loss.backward()
    w = w - LEARNING_RATE * w.grad
    loss.append(cur_loss.detach().numpy())


fig, ax = plt.subplots()
ax.plot(np.array(loss))
ax.set(xlabel="Iteracion", ylabel="Perdida")


plt.show()