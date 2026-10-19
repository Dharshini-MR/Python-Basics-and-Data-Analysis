# Month 1 - Summary of Concepts Learned

## Week 1: Introduction to Python Programming
- **Variables and data types:** a variable stores a value (`celsius = 25`). Main types: `int`, `float`, `str`, `list`.
- **Operators:** arithmetic (`+ - * /`), comparison (`>`, `==`) used to build formulas and conditions.
- **Input/output:** `print()` shows results; `input()` reads from the user.
- **Conditionals:** `if / elif / else` lets the program choose what to do (used in the calculator).
- **Loops:** `for` repeats over every item in a list; `while` repeats until a condition becomes false.
- **Practice:** temperature converter, calculator, and a script that calculates the average temperature (29.36 C) and counts days above it (3 of 7).

## Week 2: Data Structures and Functions
- **List:** ordered and changeable. **Tuple:** ordered, not changeable. **Dictionary:** key-value pairs. **Set:** only unique items.
- **Functions:** `def` packages code so it can be reused. **Lambda:** a one-line function. **Recursion:** a function that calls itself (factorial).
- **List comprehension:** a short way to build or filter a list (`[n for n in range(1, 11) if n % 2 == 0]`).
- **Practice:** sum of squares and filtering. Client project: cleaned 6 records by removing duplicates, missing ages and people under 18, leaving 2.

## Week 3: NumPy and Pandas
- **NumPy array:** fast numeric data; operations apply to all elements at once. **Broadcasting:** a smaller array is automatically stretched to match a bigger one.
- **Pandas Series and DataFrame:** a Series is one column; a DataFrame is a table.
- **Indexing:** `df["col"]` selects a column; `df.iloc[0]` selects a row by position.
- **Cleaning:** `dropna()` removes missing values; `drop_duplicates()` removes repeated rows.
- **Grouping:** `groupby()` + `mean()` gives averages per category.
- **Practice:** cleaned the sales dataset (100 rows, nothing needed removing) and found that Laptop has the highest average sale (162,050) and West the lowest region average (81,689).

## Week 4: Data Visualization with Matplotlib and Seaborn
- **Matplotlib:** the base plotting library; `plt.subplots()` builds a figure with several plots.
- **Seaborn:** built on Matplotlib; gives better-looking statistical plots such as scatter plots, histograms and heatmaps.
- **Scatter plot:** shows the relationship between two features. **Histogram:** shows how values are spread. **Heatmap:** shows correlations between many features at once.
- **Practice / dashboard:** Total Sales rises with both Price (correlation 0.65) and Quantity (0.69), while Price and Quantity are unrelated to each other (0.01). Most orders are small and a few are very large.
