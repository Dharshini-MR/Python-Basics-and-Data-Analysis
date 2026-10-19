# WEEK 4 - Data Visualization with Matplotlib and Seaborn
import pandas as pd                            # load and handle the data
import matplotlib.pyplot as plt                # Matplotlib: basic plots and the figure layout
import seaborn as sns                          # Seaborn: nicer / advanced plots such as heatmaps

df = pd.read_csv("sales_data.csv")             # load the dataset
numbers = df[["Quantity", "Price", "Total_Sales"]]   # the three numeric features we want to compare

fig, axes = plt.subplots(2, 2, figsize=(12, 9))      # one figure with 4 plots = the dashboard

sns.scatterplot(data=df, x="Price", y="Total_Sales", ax=axes[0, 0])      # scatter: does a higher price mean more sales?
axes[0, 0].set_title("Price vs Total Sales")                              # title for the plot

sns.scatterplot(data=df, x="Quantity", y="Total_Sales", ax=axes[0, 1])   # scatter: does more quantity mean more sales?
axes[0, 1].set_title("Quantity vs Total Sales")

sns.histplot(df["Total_Sales"], bins=15, ax=axes[1, 0])                  # histogram: how are order values distributed?
axes[1, 0].set_title("Distribution of Total Sales")

sns.heatmap(numbers.corr(), annot=True, cmap="coolwarm", ax=axes[1, 1])  # heatmap: correlation between all features
axes[1, 1].set_title("Correlation Heatmap")

plt.tight_layout()                             # stop the plots overlapping
plt.savefig("week4_dashboard.png", dpi=120)    # save the dashboard as an image to submit
print("Saved week4_dashboard.png")             # confirm
