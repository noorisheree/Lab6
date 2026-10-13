
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a messy product inventory dataset
data = {
    "Product": [
        "Cola", "Chips", "Milk", "Biscuits", "Juice",
        "Yogurt", "Popcorn", "Water", "Cheese", "Chocolate"
    ],
    "Category": [
        "beverages ", "SNACKS", " Dairy", "Snacks",
        "beverages", "DAIRY ", " snacks ", "Beverages",
        "dairy", "SNACKS "
    ],
    "Price": [
        "Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120",
        "Rs. 1,800", "Rs. 300", "Rs. 150", "Rs. 80",
        "Rs. 650", "Rs. 200"
    ],
    "Stock": [40, 120, 60, 90, 35, 50, 75, 150, 25, 100]
}

df = pd.DataFrame(data)

# Step 2: Clean category names
df["Category"] = df["Category"].str.strip().str.title()

# Step 3: Convert Price from text to numeric
df["Price"] = (
    df["Price"]
    .str.replace("Rs. ", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Step 4: Encode categories into numeric codes
df["Category_Code"] = df["Category"].astype("category").cat.codes

# Step 5: Print the cleaned DataFrame
print("Cleaned Product Inventory:")
print(df.to_string(index=False))

# Step 6: Calculate average price for each category
avg_price = df.groupby("Category")["Price"].mean()

# Step 7: Calculate total stock for each category
category_stock = df.groupby("Category")["Stock"].sum()

print("\nAverage Price by Category:")
print(avg_price)

print("\nStock by Category:")
print(category_stock)

# Step 8: Create two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar plot: Average price per category
axes[0].bar(avg_price.index, avg_price.values)
axes[0].set_title("Average Price by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].tick_params(axis="x", rotation=20)

# Pie chart: Share of total stock
axes[1].pie(
    category_stock.values,
    labels=category_stock.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1].set_title("Category Share of Total Stock")

# Step 9: Save the combined figure
plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()

print("\nSaved inventory_plots.png")

