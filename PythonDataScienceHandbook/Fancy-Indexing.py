"""
This file will help us understand fancy indexing
"""
# Exporing fancy indexing
import numpy as np
rand = np.random.RandomState(42)
x = rand.randint(100, size=10)
print(x)
"""
o/p:
[51 92 14 71 60 20 82 86 74 74]
"""

# Access 3 different elements
print([x[3], x[7], x[2]])
# o/p: [71, 86, 14]

# When using fancy indexing,
# the shape of the result reflects the shape of the index arrays rather than the shape of the array being indexed:
ind = np.array([
    [3,7],
    [4,5]
])
print(x[ind])

# Fancy indexing on multi-dimensional array
x = np.arange(12).reshape((3,4))
print(x)
row = np.array([0,1,2])
col = np.array([2,1,3])
print(x[row, col])
"""
Explanation for above script:
[0,2] [1,1] [2,3]
"""
# combining column vector and row vector
print(x[row[:, np.newaxis], col])
"""
o/p:
[[ 2  1  3]
 [ 6  5  7]
 [10  9 11]]
Explanation:
[0,2] [0,1] [0,3]
[1,2] [1,1] [1,3]
[2,2] [2,1] [2,3]
"""

# Combined Indexing
print(x)
print(x[2, [2, 0, 1]])

# Using slicing
print(x[1:, [2,0,1]])

# Combining fancy indexing with masking
mask = np.array([1, 0, 1, 0], dtype=bool)
print(x[row[:, np.newaxis], mask])
"""
Explanation:
Show 1st and 3rd columns for the specified rows in x array
"""

# Example: Selecting Random Points
mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)
print(X.shape) # o/p: (100,2)

import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # for plot styling

plt.scatter(X[:, 0], X[:, 1])

indices = np.random.choice(X.shape[0], 20, replace=False)
print(indices)
# o/p: [57 28 31  1 20 82  9 33 99 48 73 34 30 19 92 32 27 88 42 24]
selection = X[indices]  # fancy indexing here
print(selection.shape) # o/p: (20,2)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1],
            facecolor='none', s=200);

# Modifying values with fancy indexing
x = np.arange(10)
i = np.array([2,1,8,4])
x[i] = 99
print(x)

x = np.zeros(10)
np.add.at(x, i, 1)
print(x)
# Add 1 at the specified index position

# Example: Binning Data
np.random.seed(42)
x = np.random.randn(100)

# compute a histogram by hand
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

# find the appropriate bin for each x
i = np.searchsorted(bins, x)
np.add.at(counts, i, 1)

# plot the results
plt.plot(bins, counts, linestyle='steps');

