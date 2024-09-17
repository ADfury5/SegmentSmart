from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Select relevant features for segmentation
features = customer_data[['TotalPurchase', 'Recency', 'AvgSessionDuration']]

# Standardize the features to have mean=0 and variance=1
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply K-Means clustering to segment customers into 4 groups
kmeans = KMeans(n_clusters=4, random_state=42)
customer_data['CustomerSegment'] = kmeans.fit_predict(scaled_features)

# Assign customer segments
customer_data['CustomerSegment'] = customer_data['CustomerSegment'].map({
    0: 'High Value',
    1: 'Potential High Value',
    2: 'Low Engagement',
    3: 'Churn Risk'
})

# View the clustered data
customer_data.head()

import plotly.express as px

# Use interactive plotting to visualize customer segments
fig = px.scatter(customer_data, 
                 x='TotalPurchase', 
                 y='AvgSessionDuration', 
                 color='CustomerSegment',
                 size='Recency',
                 title='Customer Segmentation Based on Behavior')

fig.show()
