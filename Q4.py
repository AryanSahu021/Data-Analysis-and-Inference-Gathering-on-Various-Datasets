import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
data = pd.read_csv('/content/Wimbledon-women-2013.csv')

# Extract the required data
x = data['FSW.1']
y = data['SSW.1']

# Perform regression analysis
coefficients = np.polyfit(x, y, 3)
p = np.poly1d(coefficients)

# Plot the scatter plot and the curve
plt.scatter(x, y, s=10)
plt.plot(x, p(x), color='red')
plt.xlabel('First Serve Wins')
plt.ylabel('Second Serve Win Percentage')
plt.title('Scatter Plot and Regression Curve')
plt.show()
