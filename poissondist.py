import numpy
import matplotlib.pyplot as plt

num = numpy.random.poisson(3, 1000)
plt.hist(num, bins=30, density=True, color="blue", edgecolor="black")

plt.show()