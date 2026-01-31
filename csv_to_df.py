import pandas as pd

df = pd.read_csv("table_0.csv")
# print(df)

# Merge split columns
df["Description"] = df["Unnamed: 0"].fillna("") + " " + df["Description"].fillna("")
df["Category"] = df["Unnamed: 1"].fillna("") + " " + df["Category"].fillna("")

# Drop junk columns
df = df[["Date", "Description", "Category", "Income (Credit)", "Expense (Debit)"]]

# Remove commas in numbers
df["Income (Credit)"] = df["Income (Credit)"].replace(',', '', regex=True).astype(float)
df["Expense (Debit)"] = df["Expense (Debit)"].replace(',', '', regex=True).astype(float)

df.to_csv("final_clean.csv", index=False)

