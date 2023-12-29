import pandas as pd
import matplotlib.pyplot as plt

# Load the data for Australian Open and French Open
ausopen = pd.read_csv('/content/AusOpen-men-2013.csv')
frenchopen = pd.read_csv('/content/FrenchOpen-men-2013.csv')
wimbledon = pd.read_csv('/content/Wimbledon-men-2013.csv')
usopen = pd.read_csv('/content/USOpen-men-2013.csv')
# Calculate the average number of unforced errors, winners, aces, and double faults
ausopen_stats = ausopen[['UFE.1', 'WNR.1', 'ACE.1', 'DBF.1']].mean()
frenchopen_stats = frenchopen[['UFE.1', 'WNR.1', 'ACE.1', 'DBF.1']].mean()
wimbledon_stats = wimbledon[['UFE.1', 'WNR.1', 'ACE.1', 'DBF.1']].mean()
usopen_stats = usopen[['UFE.1', 'WNR.1', 'ACE.1', 'DBF.1']].mean()


# Plot the comparison graph for double faults
fig, ax = plt.subplots()
ax.bar(['AusOpen', 'FrenchOpen','Wimbledon','USOpen'], [ausopen_stats[3], frenchopen_stats[3], wimbledon_stats[3], usopen_stats[3]])
ax.set_ylabel('Average Number')
ax.set_title('Comparison of Double Faults')
plt.show()
