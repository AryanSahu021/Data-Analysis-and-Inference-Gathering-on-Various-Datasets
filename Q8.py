import pandas as pd
import matplotlib.pyplot as plt

# Load the data for US Open
usopen = pd.read_csv('/content/FrenchOpen-men-2013.csv')

# Extract the required columns
games_won_1 = usopen['FNL.1']
games_won_2 = usopen['FNL.2']

# Plot the scatter plot
plt.scatter(games_won_1, games_won_2)
plt.xlabel('Final Number of Games Won by Player 1')
plt.ylabel('Final Number of Games Won by Player 2')
plt.title('Comparison of Final Number of Games Won by Players in French Open')
plt.show()
