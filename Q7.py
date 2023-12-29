import pandas as pd
import matplotlib.pyplot as plt

# Load the data for US Open
usopen = pd.read_csv('/content/USOpen-men-2013.csv')

# Get the final number of games won by player 1 and player 2
gameswon_p1 = usopen['FNL1']
gameswon_p2 = usopen['FNL2']

# Plot the histograms side by side
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 10))
ax1.hist(gameswon_p1, bins=10)
ax1.set_xlabel('Final Number of Games Won')
ax1.set_ylabel('Frequency')
ax1.set_title('Player 1')

ax2.hist(gameswon_p2, bins=10)
ax2.set_xlabel('Final Number of Games Won')
ax2.set_ylabel('Frequency')
ax2.set_title('Player 2')

plt.show()
