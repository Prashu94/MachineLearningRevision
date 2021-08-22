"""
This file will help understand the comparison, masking and boolean logic
"""
# Example: Counting Rainy Days
import pandas as pd
import numpy as np
rainfall = pd.read_csv("H:\\LearningWorkspace\\MachineLearning\\MachineLearningRevision\\PythonDataScienceHandbook"
                       "\\data"
                   "\\Seattle2014.csv")
# Store only the PRCP columns
rainfall = rainfall['PRCP'].values
# Convert the mm to inches
inches = rainfall / 254.0
print(inches.shape) # o/p: 365
# The data contains the 365 values givening rainfall inches for all the year
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

plt.hist(inches,40)

# Comparison operators as ufuncs
x = np.array([1, 2, 3, 4, 5])
print(x<3)
# o/p: [ True  True False False False]
print(x>3)
# o/p: [False False False  True  True]
print(x<=3)
# o/p: [ True  True  True False False]
print(x>=3)
# o/p: [False False  True  True  True]
print(x!=3)
# o/p: [ True  True False  True  True]
print(x==3)
# o/p: [False False  True False False]

# 2 Dimensional Arrays
rng = np.random.RandomState(0)
x = rng.randint(10, size=(3,4))
print(x)
"""
o/p:
[[5 0 3 3]
 [7 9 3 5]
 [2 4 7 6]]
"""
print(x<6)


# Working With Boolean Arrays
print(x)
# 1. Counting entries
np.count_nonzero(x < 6)
# 2. np.sum : false is interpreted as 0 and true is interpreted as 1
np.sum(x < 6)
# 3. how many values are less than 6 in each row? axis = 1 (row) axis = 0 (column)
np.sum(x < 6, axis=1)
# o/p: array([4, 2, 2])
# 4. are there any values greater than 8?
np.any(x > 8) # any method gives True if any condition matches
# o/p: True
# are there any value less than 0?
np.any(x < 0)
# o/p: False
# are all values greater than 10?
np.all(x > 10) # all method gives False if the condition is False
# o/p: False
# are all values less than 10?
np.all(x < 10)
# are all the values equal to 6?
np.all(x == 6) # False
# Using any and all for particular axis
# are all values in each row less than 8?
np.all(x < 8, axis=1)

# Boolean Operators
np.sum((inches > 0.5) & (inches < 1))
# o/p: 29 ( 29 days with rainfalls between 0.5 and 1 inches)
print("Number days without rain:      ", np.sum(inches == 0))
print("Number days with rain:         ", np.sum(inches != 0))
print("Days with more than 0.5 inches:", np.sum(inches > 0.5))
print("Rainy days with < 0.2 inches  :", np.sum((inches > 0) &
                                                (inches < 0.2)))

# Boolean Arrays as masks
print(x)
# Get the array values which is less than 5
print(x[x<5])
# o/p: [0 3 3 3 2 4]

# Construct a mask for all rainy days
rainy = (inches>0) # inches > 0 then rain
# construct a mask for all summer days(June 21st is the 172nd day)
days = np.arange(365)
summer = (days > 172) & (days < 262)
print(rainy)
print(summer)
print("Median precip on rainy days in 2014 (inches):   ",
      np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches):  ",
      np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches): ",
      np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):",
      np.median(inches[rainy & ~summer]))



