import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
filename=r"C:\Users\aryan\Downloads\Tennis-Major-Tournaments-Match-Statistics\Wimbledon-men-2013.csv"
# Load CSV data into a pandas DataFrame
tennis_data = pd.read_csv(filename)

# Scatter plot of FSP vs. Match Outcome
sns.scatterplot(x='FSP.1',y='Result', data=tennis_data)
plt.xlabel('First Serve Percentage (FSP)')
plt.ylabel('Match Outcome (Win/Loss)')
plt.title('Scatter plot of FSP vs. Match Outcome')
plt.show()

# Box plot of FSP by Match Outcome
sns.boxplot(x='Result', y='FSP.1', data=tennis_data)
plt.xlabel('Match Outcome (Win/Loss)')
plt.ylabel('First Serve Percentage (FSP)')
plt.title('Box plot of FSP by Match Outcome')
plt.show()