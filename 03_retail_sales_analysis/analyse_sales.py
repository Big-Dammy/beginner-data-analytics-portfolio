# Import pandas for data analysis and matplotlib for simple charts.
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Locate this project folder and prepare an outputs folder.
HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "data" / "retail_transactions.csv"
OUTPUT_FOLDER = HERE / "outputs"
OUTPUT_FOLDER.mkdir(exist_ok=True)

# Read the CSV and tell pandas that the date column contains dates.
data = pd.read_csv(DATA_FILE, parse_dates=["date"])

# Print a first look at the data so we know how many rows and columns we have.
print("Dataset size:", data.shape)
print("Missing values before cleaning:")
print(data.isna().sum())

# Replace missing region names with the word Unknown instead of deleting those sales.
data["region"] = data["region"].fillna("Unknown")

# Make a monthly column so transactions can be grouped by month.
data["month"] = data["date"].dt.to_period("M").astype(str)

# Add up sales for each product and sort from highest to lowest.
sales_by_product = data.groupby("product", as_index=False)["sales_amount"].sum()
sales_by_product = sales_by_product.sort_values("sales_amount", ascending=False)
sales_by_product.to_csv(OUTPUT_FOLDER / "sales_by_product.csv", index=False)

# Add up sales for each region.
sales_by_region = data.groupby("region", as_index=False)["sales_amount"].sum()
sales_by_region = sales_by_region.sort_values("sales_amount", ascending=False)
sales_by_region.to_csv(OUTPUT_FOLDER / "sales_by_region.csv", index=False)

# Add up sales for each month so we can inspect the trend over time.
monthly_sales = data.groupby("month", as_index=False)["sales_amount"].sum()
monthly_sales.to_csv(OUTPUT_FOLDER / "monthly_sales.csv", index=False)

# Print useful headline figures to the screen.
print(f"Total sales value: £{data['sales_amount'].sum():,.2f}")
print("Top product by sales:")
print(sales_by_product.head(1).to_string(index=False))
print("Top region by sales:")
print(sales_by_region.head(1).to_string(index=False))

# Draw a bar chart showing total sales by product.
plt.figure(figsize=(9, 5))
plt.bar(sales_by_product["product"], sales_by_product["sales_amount"])
plt.title("Sales by Product (Synthetic Data)")
plt.xlabel("Product")
plt.ylabel("Sales amount (£)")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_FOLDER / "sales_by_product.png")
plt.close()

# Draw a line chart showing monthly sales.
plt.figure(figsize=(11, 5))
plt.plot(monthly_sales["month"], monthly_sales["sales_amount"], marker="o", markersize=3)
plt.title("Monthly Sales (Synthetic Data)")
plt.xlabel("Month")
plt.ylabel("Sales amount (£)")
plt.xticks(rotation=60, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_FOLDER / "monthly_sales.png")
plt.close()

print("Finished. Check the outputs folder for summaries and charts.")
