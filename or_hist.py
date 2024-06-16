import pandas as pd
data = pd.read_csv(r"c:\Users\dhath\Downloads\MSDS-Orientation-Computer-Survey(in).csv")

import matplotlib.pyplot as plt
plt.hist(data["RAM (in GB)"], bins=40, color="blue", edgecolor="black")
plt.title("RAM Size of Students' Computers")
plt.xlabel("RAM (in GB)")
plt.ylabel("Number of Students")

plt.show()

data.to_csv("computerdata.csv")