import pandas as pd
import matplotlib.pyplot as plt

# Load the data for Australian Open
ausopen = pd.read_csv('/content/AusOpen-men-2013.csv')

# Get the required data
net_attempted = ausopen['NPW.1']
net_won = ausopen['NPA.1']

# Plot the relation
plt.scatter(net_attempted, net_won)
plt.xlabel('Net Points Attempted')
plt.ylabel('Net Points Won')
plt.title('Relation between Net Points Attempted and Won')
plt.show()
