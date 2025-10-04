import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

def split_data(X, y, test_size=0.2, random_state=42):
    np.random.seed(random_state)
    n_samples = X.shape[0]
    test_samples = int(n_samples * test_size)

    indices = np.random.permutation(n_samples)
    test_indices = indices[:test_samples]
    train_indices = indices[test_samples:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

