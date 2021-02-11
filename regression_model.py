import numpy as np


def regression(x, y):
    w = np.linalg.lstsq(x, y, rcond=None)[0]
    return w


def cost_function(x, y, theta):
    return np.sum((np.dot(x, theta) - y) ** 2) / 2 * len(y)


def gradient_decent(x, y, learning_rate, theta, epochs):
    cost_history = []

    for i in range(epochs):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        gradient = np.dot(x.T, loss) / len(y)
        theta = theta - learning_rate * gradient
        cost = cost_function(x, y, theta)
        cost_history.append(cost)

    return theta, cost_history


def fit(x, y, learning_rate, epochs):
    theta = np.zeros(x.shape[1])
    theta,cost = gradient_decent(x,y,learning_rate,theta,epochs)

    return theta,cost