import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt

sampleNo = a;
mu = b
sigma = c
np.random.seed(0)
s = np.random.normal(mu, sigma, sampleNo )
plt.hist(s, 30, normed=True)

