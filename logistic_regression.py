import numpy as np
import matplotlib.pyplot as plt

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X, y):
        self.weights = np.zeros((X.shape[1], 1))
        self.bias = 0
        for _ in range(self.num_iterations):
            z = np.dot(X, self.weights) + self.bias
            A = self.sigmoid(z)
            cost = -np.mean(y * np.log(A) + (1 - y) * np.log(1 - A))
            dz = A - y
            dw = np.dot(X.T, dz) / X.shape[0]
            db = np.mean(dz)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict_proba(self, X):
        z = np.dot(X, self.weights) + self.bias
        return self.sigmoid(z)
    
    def predict(self, X, threshold=0.5):
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int)

np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = (4 + 3 * X + np.random.randn(100, 1)) > 6

model = LogisticRegression()
model.fit(X, y)

plt.scatter(X, y, color='blue')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Logistic Regression')

X_decision = np.linspace(0, 2, 100)
y_decision = model.predict(X_decision.reshape(-1, 1))
plt.plot(X_decision, y_decision, color='red', linestyle='--')

plt.show()
