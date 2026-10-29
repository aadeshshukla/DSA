import numpy as np
import pandas as pd

# ---------------------------------------------------------
# 1. Loading Data
# ---------------------------------------------------------
# Load from CSV (or create a sample DataFrame for testing)
data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Department": ["Sales", "Engineering", "Sales", "HR", "Engineering", None],
    "Salary": [50000, 85000, None, 45000, 92000, 60000],
    "JoinDate": [
        "2021-01-15",
        "2019-06-01",
        "2020-09-12",
        "2022-03-01",
        "2018-11-20",
        "2023-05-10",
    ],
}
df = pd.DataFrame(data)

# To read from an external file instead:
# df = pd.read_csv("data.csv")

# ---------------------------------------------------------
# 2. Inspecting the Dataset
# ---------------------------------------------------------
print("--- Initial Inspection ---")
print(df.head())          # First 5 rows
print(df.info())          # Data types and non-null counts
print(df.describe())      # Summary statistics for numeric fields

# ---------------------------------------------------------
# 3. Data Cleaning
# ---------------------------------------------------------
# Convert data types (e.g., string to datetime)
df["JoinDate"] = pd.to_datetime(df["JoinDate"])

# Check for missing values
missing_counts = df.isnull().sum()

# Handle missing values:
# - Fill categorical missing data with a default label
df["Department"] = df["Department"].fillna("Unassigned")

# - Impute numerical missing data (e.g., with department median or overall mean)
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Remove duplicate rows if any exist
df = df.drop_duplicates()

# ---------------------------------------------------------
# 4. Data Transformation & Filtering
# ---------------------------------------------------------
# Add derived columns
df["Bonus"] = df["Salary"] * 0.10
df["TotalCompensation"] = df["Salary"] + df["Bonus"]

# Filter rows (e.g., Engineering staff with Salary > 80,000)
high_earning_engineers = df[
    (df["Department"] == "Engineering") & (df["Salary"] > 80000)
]

# Sort records
df = df.sort_values(by="Salary", ascending=False)

# ---------------------------------------------------------
# 5. Aggregation & Grouping
# ---------------------------------------------------------
# Group by department and compute summary metrics
dept_summary = (
    df.groupby("Department")
    .agg(
        EmployeeCount=("EmployeeID", "count"),
        AvgSalary=("Salary", "mean"),
        MaxSalary=("Salary", "max"),
    )
    .reset_index()
)

print("\n--- Department Summary ---")
print(dept_summary)

# ---------------------------------------------------------
# 6. Exporting Processed Data
# ---------------------------------------------------------
# df.to_csv("cleaned_data.csv", index=False)
# dept_summary.to_excel("department_summary.xlsx", index=False)
