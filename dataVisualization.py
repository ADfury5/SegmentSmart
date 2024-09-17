import matplotlib.pyplot as plt
import seaborn as sns

# Visualize the distribution of Total Purchase
plt.figure(figsize=(10, 6))
sns.histplot(customer_data['TotalPurchase'], kde=True, bins=30)
plt.title('Distribution of Total Purchase Value')
plt.show()

# Scatter plot of Average Session Duration vs Total Purchase
plt.figure(figsize=(10, 6))
sns.scatterplot(x='AvgSessionDuration', y='TotalPurchase', data=customer_data, hue='CustomerSegment')
plt.title('Average Session Duration vs Total Purchase')
plt.show()
