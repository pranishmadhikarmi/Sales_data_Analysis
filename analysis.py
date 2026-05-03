
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data/sales_data.csv')

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# Total Revenue
total_revenue = df['Total_Sales'].sum()
print('Total Revenue:', total_revenue)

# Best-selling products
best_products = df.groupby('Product_Name')['Total_Sales'].sum().sort_values(ascending=False)
print('\nBest Selling Products:\n', best_products)

# Monthly sales trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

# Category distribution
category_sales = df.groupby('Category')['Total_Sales'].sum()

# ---------------- Visualizations ----------------

# Bar chart - Best selling products
best_products.plot(kind='bar', title='Best Selling Products')
plt.show()

# Line chart - Monthly trend
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend')
plt.show()

# Pie chart - Category distribution
category_sales.plot(kind='pie', autopct='%1.1f%%', title='Category Distribution')
plt.ylabel('')
plt.show()
