import numpy
import matplotlib.pyplot as plt

mu, sigma = 0, 1
num = numpy.random.normal(mu, sigma, 1000)
plt.hist(num, bins=10, density=True, alpha=0.6, color="blue", edgecolor="black")

xmin, xmax = plt.xlim()
x = numpy.linspace(xmin, xmax, 100)
p = (1/(numpy.sqrt(2 * numpy.pi) * sigma)) * numpy.exp(-0.5 * ((x - mu) / sigma)**2)
plt.plot(x, p, 'k', linewidth=2)

plt.show()
