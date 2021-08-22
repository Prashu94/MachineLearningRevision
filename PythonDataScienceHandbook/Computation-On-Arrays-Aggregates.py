"""
This file will help us understand the aggregation operations.
"""

# 1. Summing the Values in the Array
import numpy as np
L = np.random.random(100)
print(sum(L))
# o/p: 50.461758453195614

# 2.Minimum and Maxium
big_array = np.random.rand(1000000)
print("Minimum : ", np.min(big_array))
print("Maximum : ", np.max(big_array))

# 3. Multi-dimensional Aggregates
M = np.random.random((3,4))
print(M)
print(M.sum())
# o/p: 6.0850555667307118
"""
Aggregation function takes an additional argument specifying the axis along which the aggregation is computed.
"""
# Minimum in each column axis = 0
print(M.min(axis = 0))
# Maximum from each row axis = 1
print(M.max(axis = 1))

# Example using real data
import pandas as pd
data = pd.read_csv("H:\\LearningWorkspace\\MachineLearning\\MachineLearningRevision\\PythonDataScienceHandbook\\data"
                   "\\president_heights.csv")
print(data.head())
# Store the value of the height column in the height array
heights = np.array(data['height(cm)'])
print(heights)

"""
Summary Statistics to be calculated on the heights array
mean, std.dev, min, max
25th percentile, Median, 75th percentile
"""
print("Mean Height = ", np.mean(heights))
print("Standard Deviation = ", np.std(heights))
print("Minimum = ", np.min(heights))
print("Maximum = ", np.max(heights))
print("25th Percentile = ", np.percentile(heights, 25))
print("Median = ", np.median(heights))
print("75th Percentile = ", np.percentile(heights, 75))

