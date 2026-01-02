import pandas as pd

# Step 1: Read raw data
df = pd.read_csv("data/raw/retail_sales.csv")

# Step 2: Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Step 3: Remove duplicate rows
df = df.drop_duplicates()

# Step 4: Remove rows with missing values
df = df.dropna()

# Step 5: Convert order_date to date format
df['order_date'] = pd.to_datetime(df['order_date'])

# Step 6: Save cleaned data
df.to_csv("data/processed/clean_retail_sales.csv", index=False)

print("Retail sales data cleaned successfully")
