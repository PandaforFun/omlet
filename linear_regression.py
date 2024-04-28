import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self):
        self.coefficients = None
    
    def fit(self, X, y):
        X_bias = np.c_[np.ones((X.shape[0], 1)), X]
        self.coefficients = np.linalg.inv(X_bias.T.dot(X_bias)).dot(X_bias.T).dot(y)
    
    def predict(self, X):
        X_bias = np.c_[np.ones((X.shape[0], 1)), X]
        predictions = X_bias.dot(self.coefficients)
        return predictions

np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

model = LinearRegression()
model.fit(X, y)

X_new = np.array([[0], [2]])
predictions = model.predict(X_new)

plt.scatter(X, y, color='blue', label='Original data')
plt.plot(X_new, predictions, color='red', label='Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()
