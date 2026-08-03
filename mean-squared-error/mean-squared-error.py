import numpy as np

def mean_squared_error(y_pred, y_true):
    y = np.array(y_true)
    y_hat = np.array(y_pred)
    return sum((y - y_hat) ** 2) / len(y)
