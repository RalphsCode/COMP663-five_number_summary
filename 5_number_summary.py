# Assignment 1 Question 2
# Author: Ralph Godkin

# IMPORTS
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
hitters_df = pd.read_csv("Module-2/test_hitters.csv")

# There are 17 rows
# Primary key, Quality, Speed, Angle

# Find (1)mean, (2)weighted mean, (3)median, (4)mode, (5)Standard Deviation, (6)mad, (7)max, (8)range

print("5 Category Summary: ", hitters_df.describe())

# Plots a box plot
sns.boxplot(data=hitters_df, width=0.35)

plt.show()




