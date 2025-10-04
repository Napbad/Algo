import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_boston_data():
    try:
        url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
        boston = pd.read_csv(url)
        X = boston.drop('medv', axis=1).values
        y = boston['medv'].values
        # for i in range(10):
            # print(f"X[{i}]: {X[i]}")
            # print(f"y[{i}]: {y[i]}")

        print("load data success")
        return X, y
    except Exception as e:
        print(f"error detected: {e}")
        np.random.seed(42)
        X = np.random.rand(506, 13) * 100
        y = X.dot(np.random.rand(13)) + np.random.randn(506) * 10
        return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    np.random.seed(random_state)
    n_samples = X.shape[0]
    test_samples = int(n_samples * test_size)

    indices = np.random.permutation(n_samples)
    test_indices = indices[:test_samples]
    train_indices = indices[test_samples:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

def standard_scaler(X_train, X_test):
    mean = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    std [std == 0] = 1.0

    x_train_std = (X_train - mean) / std
    x_test_std = (X_test - mean) / std

    return x_train_std, x_test_std

def custom_mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)** 2)

def custom_r2_score(y_true, y_pred):
    ss_total = np.sum((y_true - np.mean(y_true))**2)
    ss_residual = np.sum((y_true - y_pred)**2)
    return 1 - ss_residual / ss_total

class LinearRegression:
    def __init__(self, leaning_rate=0.01, n_iters=1000):
        self.leaning_rate = leaning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        self.cost_history = []
        self.grad = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0
        for i in range(self.n_iters):
            y_predict = np.dot(X, self.weights) + self.bias
            mean_squared_loss = custom_mean_squared_error(y_predict, y)
            self.cost_history.append(mean_squared_loss)

            tmp =  np.dot(X.T, (y_predict - y))
            dw = 2 / n_samples * tmp
            db = 2 / n_samples * np.sum(y_predict - y)

            self.weights = self.weights - dw * self.leaning_rate
            self.bias = self.bias - db * self.leaning_rate
            if i % 1000 == 0:
                print(f"Iteration: {i}")
                print(f"MSE: {mean_squared_loss}")
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

if __name__ == "__main__":
    X, y = load_boston_data()

    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)
    X_train, X_test = standard_scaler(X_train, X_test)
    model = LinearRegression(leaning_rate=0.001, n_iters=10000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"MSE: {custom_mean_squared_error(y_test, y_pred)}")