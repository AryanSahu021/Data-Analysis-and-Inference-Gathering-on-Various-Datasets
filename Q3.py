import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
filename=r"C:\Users\aryan\Downloads\Tennis-Major-Tournaments-Match-Statistics\Wimbledon-women-2013.csv"

# Load the dataset
df = pd.read_csv(filename)

# Group the data by round and calculate the average UFE for Player 1 and Player 2
grouped = df.groupby('Round').mean()
avg_fsp_1 = grouped['UFE.1']
avg_fsp_2 = grouped['UFE.2']

# Create a line plot to visualize the average UFE for Player 1 and Player 2 against the round
plt.figure(1)
plt.plot(avg_fsp_1.index, avg_fsp_1, label='Player 1')
plt.plot(avg_fsp_2.index, avg_fsp_2, label='Player 2')

# Set plot labels and title
plt.xlabel('Round')
plt.ylabel('Average Unforced Errors')
plt.title('Average Unforced Errors vs. Round of Tournament')
plt.legend()

# Group the data by round and calculate the average DBF for Player 1 and Player 2
grouped = df.groupby('Round').mean()
avg_fsp_1 = grouped['DBF.1']
avg_fsp_2 = grouped['DBF.2']
plt.figure(2)
# Create a line plot to visualize the average DBF for Player 1 and Player 2 against the round
plt.plot(avg_fsp_1.index, avg_fsp_1, label='Player 1')
plt.plot(avg_fsp_2.index, avg_fsp_2, label='Player 2')

# Set plot labels and title
plt.xlabel('Round')
plt.ylabel('Average Double Faults Committed')
plt.title('Average Double Faults Committed vs. Round of Tournament')
plt.legend()

# Show the plot
plt.show()

