import numpy
import matplotlib.pyplot as plt

df = 3
num = numpy.random.chisquare(df, 1000)

plt.hist(num, bins=30, density=True, color="blue", edgecolor="black")
plt.show()