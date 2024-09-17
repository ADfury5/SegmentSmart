import pandas as pd

# Load customer data (e.g., CSV with columns like 'CustomerID', 'PurchaseAmount', 'SessionDuration', 'LastPurchaseDate', etc.)
customer_data = pd.read_csv('customer_data.csv')

# Check for missing values
customer_data.isnull().sum()

# Fill or drop missing values based on requirements
customer_data.fillna(0, inplace=True)

# Create new features such as Total Purchase Value and Average Session Duration
customer_data['TotalPurchase'] = customer_data.groupby('CustomerID')['PurchaseAmount'].transform('sum')
customer_data['AvgSessionDuration'] = customer_data.groupby('CustomerID')['SessionDuration'].transform('mean')

# Drop duplicates
customer_data.drop_duplicates(subset=['CustomerID'], inplace=True)

# Standardize dates to calculate recency
customer_data['Recency'] = (pd.to_datetime('today') - pd.to_datetime(customer_data['LastPurchaseDate'])).dt.days
