import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Reshape to a 2D array
y = np.array([2, 4, 6, 8, 10])

# Create a LinearRegression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict values using the model
predicted_y = model.predict(X)

# Plot the original data and the regression line
plt.scatter(X, y, label='Original Data')
plt.plot(X, predicted_y, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.legend()
plt.show()

# Print the model's coefficients
print('Intercept:', model.intercept_)
print('Slope:', model.coef_)
