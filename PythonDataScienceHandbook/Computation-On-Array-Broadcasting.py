"""
The scripts in the file will help understand the Broadcastig computation provide by NumPy
"""
import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print(a+b)

# Matrix 3 x 3 matrix
M = np.ones(shape=(3, 3))
print(M)
"""
o/p:
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
"""
# Operation
print(M+a)
"""
o/p:
[[1. 2. 3.]
 [1. 2. 3.]
 [1. 2. 3.]]
Note: Here the one dimensional Array a is stretched/broadcasted accross the second dimension in order to match the 
shape of M
"""

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
print(a)
print(b)
"""
o/p:
[0 1 2]
Vertical vectors
[[0]
 [1]
 [2]]
"""
print(a+b)
"""
o/p:
[[0 1 2]
 [1 2 3]
 [2 3 4]]
"""

# 1. Broadcasting Example 1:
M = np.ones(shape=(2,3))
a = np.arange(3)
print(M)
print(a)
"""
o/p:
M
[[1. 1. 1.]
 [1. 1. 1.]]
a
[0 1 2]
"""
print(M.shape) # o/p: 2,3
print(a.shape) # o/p: 3,

"""
Rule 1: array a has a fewer dimensions, so we pad it on the left with ones.
M.shape 2,3
a.shape 1,3
Rule 2: we see that the first dimension disagrees, so we stretch the dimension to match
M.shape 2,3
a.shape 2,3
"""
print(M+a)

# Broadcasting example 2
a = np.arange(3).reshape((3, 1))
b = np.arange(3)
print(a)
print(b)
"""
o/p:
a
[[0]
 [1]
 [2]]
b
[0 1 2]
"""
print(a+b)
"""
o/p:
[[0 1 2]
 [1 2 3]
 [2 3 4]]
"""

# 3. Broadcasting Example 3
M = np.ones((3,2))
a = np.arange(3)
print(M.shape) # o/p: (3,2)
print(a.shape) # o/p: (3,)

# Note the above matches rule 3, hence addition will give error as the dimensions does not match
# Hence we change the shape of the array a
a[:,np.newaxis].shape
print(M+a[:, np.newaxis])

