import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a messy 15-day weather log
data = {
    "Date": [
        "2026-09-01", "2026-09-02", "2026-09-03",
        "2026-09-04", "2026-09-05", "2026-09-06",
        "2026-09-07", "2026-09-08", "2026-09-09",
        "2026-09-10", "2026-09-11", "2026-09-12",
        "2026-09-13", "2026-09-14", "2026-09-15"
    ],
    "City": [
        " islamabad ", "LAHORE", "karachi ",
        " Islamabad", "LAHORE ", "karachi",
        " ISLAMABAD", "lahore", " KARACHI ",
        "islamabad", " Lahore", "KARACHI ",
        " Islamabad ", "LAHORE", "karachi"
    ],
    "Temperature": [
        "32C", "35C", "34C", "30C", "31C",
        "36C", "29C", "33C", "37C", "28C",
        "32C", "35C", "27C", "30C", "34C"
    ],
    "Humidity": [
        55, 60, None, 70, 50,
        62, 58, None, 45, 65,
        55, None, 60, 48, 58
    ],
    "Condition": [
        "sunny", " CLOUDY ", "Rainy",
        " Sunny ", "cloudy", " SUNNY",
        "rainy ", "Cloudy", " sunny",
        "CLOUDY", "Rainy", " sunny ",
        " cloudy ", "SUNNY", "sunny"
    ]
}

df = pd.DataFrame(data)

# Add one duplicated row
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

print("Original Weather Log:")
print(df.to_string(index=False))

# Step 2: Clean text columns
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

# Step 3: Remove C from Temperature and convert to numbers
df["Temperature"] = (
    df["Temperature"]
    .str.replace("C", "", regex=False)
    .astype(float)
)

# Step 4: Convert Date text into datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Step 5: Remove the duplicated row
df = df.drop_duplicates().reset_index(drop=True)
print("\nRows after dropping duplicates:", len(df))

# Step 6: Fill missing Humidity values with the median
humidity_median = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(humidity_median)

print("Missing Humidity filled with median:", humidity_median)

# Step 7: One-hot encode the Condition column
condition_encoded = pd.get_dummies(
    df["Condition"], prefix="Condition", dtype=int
)

print("\nEncoded Condition Columns:")
print(condition_encoded.columns.to_list())

print("\nOne-Hot Encoded Data:")
print(condition_encoded.to_string(index=False))

# Step 8: Calculate correlation
correlation = df["Temperature"].corr(df["Humidity"])
print("\nCorrelation (Temperature, Humidity):", round(correlation, 2))

# Step 9: Count days for each weather condition
condition_counts = df["Condition"].value_counts()

print("\nCondition counts:")
print(condition_counts.to_string())

# Step 10: Create a 2 x 2 dashboard with four plots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Temperature over Date
axes[0, 0].plot(
    df["Date"], df["Temperature"],
    marker="o", linestyle="-"
)
axes[0, 0].set_title("Temperature Over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=45)

# Plot 2: Temperature vs Humidity
axes[0, 1].scatter(df["Temperature"], df["Humidity"])
axes[0, 1].set_title("Temperature vs Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity (%)")

# Plot 3: Pie chart of weather conditions
axes[1, 0].pie(
    condition_counts.values,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 0].set_title("Weather Condition Distribution")

# Plot 4: Temperature histogram
axes[1, 1].hist(df["Temperature"], bins=6, edgecolor="black")
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

# Overall dashboard title
fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Step 11: Save the dashboard image
plt.savefig("weather_dashboard.png", dpi=300, bbox_inches="tight")
print("\nSaved weather_dashboard.png")

plt.show()