# WEEK 3 - NumPy and Pandas for Data Manipulation
import numpy as np                             # NumPy: fast arrays and maths
import pandas as pd                            # Pandas: tables (DataFrames)

# ---------- Hands-on: NumPy ----------
a = np.array([1, 2, 3, 4])                     # a NumPy array
print("a * 2 =", a * 2)                        # operation applies to every element at once
matrix = np.array([[1, 2, 3], [4, 5, 6]])      # a 2-D array (2 rows, 3 columns)
print("Broadcasting:", matrix + np.array([10, 20, 30]))   # broadcasting: the row [10,20,30] is added to every row
print("Mean of a:", a.mean())                  # built-in statistics

# ---------- Client project: clean and aggregate the sales dataset ----------
df = pd.read_csv("sales_data.csv")             # load the CSV into a DataFrame
print(df.head(3))                              # look at the first 3 rows
print("Rows before cleaning:", len(df))        # size before cleaning

df = df.dropna()                               # remove rows with missing values (this file has none)
df = df.drop_duplicates()                      # remove duplicate rows (this file has none)
print("Rows after cleaning:", len(df))         # size after cleaning

print("Total_Sales column (Series):")          # a single column is a Series
print(df["Total_Sales"].head(3))
print("Row 0 by position:", df.iloc[0]["Product"])   # indexing: iloc picks rows by position

print("Average Total_Sales:", df["Total_Sales"].mean())   # overall average
print(df.groupby("Product")["Total_Sales"].mean())        # grouping: average sales per product
print(df.groupby("Region")["Total_Sales"].mean())         # grouping: average sales per region
