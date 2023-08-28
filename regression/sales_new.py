import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
data_url='https://raw.githubusercontent.com/redashu/Datasets/master/advertising.csv'
# creating data from using URL data
df=pd.read_csv(data_url)
# Define the independent variables (features)
X = df[['TV', 'Radio', 'Newspaper']]

# Define the dependent variable
y = df['Sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a LinearRegression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict sales for the test data
y_pred = model.predict(X_test)

# Print the coefficients and intercept
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)
coefficients = model.coef_

# Plot actual vs. predicted values for the test data
plt.scatter(y_test, y_pred)
plt.plot([min(y_test), max(y_test)], [min(y_pred), max(y_pred)], linestyle='--', color='red', linewidth=2)

plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Actual vs. Predicted Sales')
plt.show()

for feature, coefficient in zip(X.columns, coefficients):
    print(f'{feature}: {coefficient}')
