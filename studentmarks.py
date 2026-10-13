
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the messy student dataset
data = {
    "Name": [
        " ali", "SARA ", "bilal", " Ayesha",
        "HAMZA", "zain ", "Noor", " usman "
    ],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

# Step 2: Clean student names
df["Name"] = df["Name"].str.strip().str.title()

# Step 3: Convert marks to numeric values
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Step 4: Replace the absent student's marks with the mean
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

# Step 5: Print the cleaned DataFrame
print("Cleaned Student Marks:")
print(df)

# Step 6: Draw a bar plot
plt.figure(figsize=(9, 5))
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()

# Step 7: Save the plot
plt.savefig("marks_bar.png")
plt.show()

print("Saved marks_bar.png")
