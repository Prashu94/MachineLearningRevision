"""
This file will hep us understand the basics of Numpy Array and the operations
"""

# 1. Numpy Array Attributes
import numpy as np
# Note: To use numpy's random number generator, we can set a seed value to generate the same random array each time.
np.random.seed(0)

# One Dimensional Array
x1 = np.random.randint(10, size=6)
# Two Dimensional Array
x2 = np.random.randint(10, size=(3, 4))
# Three Dimensional Array
x3 = np.random.randint(10, size=(3, 4, 5))

print(x1)
print(x2)
print(x3)

# To check dimensions of each array
print("x3 ndim : ", x3.ndim)
"""
o/p:
3
"""
print("x3 shape: ", x3.shape)
"""
o/p:
(3,4,5)
"""
print("x3 size: ", x3.size)
"""
o/p:
60
"""

# To check the data type
print("dtype :", x3.dtype)
"""
o/p:
int32
"""

# Other Attributes
print("itemsize: ", x3.itemsize, "bytes")
# o/p: 4 bytes
print("nbytes: ", x3.nbytes, "bytes")
# o/p: 240 bytes(size*itemsize)

# 2. Array indexing
# One Dimensional
print(x1)
print(x1[0]) # o/p: 3
print(x1[4]) # o/p: 0
print(x1[-1]) # o/p: 1
print(x1[-2]) # o/p: 0

# Multi Dimensional Array
print(x2)
print(x2[0, 0]) # o/p: 5
print(x2[2, 0]) # o/p: 4
print(x2[2, -1]) # o/p: 3

# To modify the index location value
x2[0,0] = 12
print(x2[0,0])

# Note: Unlike Lists Python Arrays have a fixed type.

# Exercise: 3-D Array Indexing
print(x3)
print(x3[1,])
print(x3[1,2,0])

# 3. Array Slicing

# One Dimensional
x = np.arange(10)
print(x)
# First Five elements
print(x[:5])
# ELements after index 5
print(x[5:])
# Middle Sub Array
print(x[4:7])
# Every other element(alternate elements even elements)
print(x[::2])
# Every other element starting at index 1(odd elements)
print(x[1::2])
# Reverse array elements
print(x[::-1])
# Reverse every other from index 5
print(x[5::-1])

#Multi Dimensional Sub Arrays
print(x2)

# Two rows, Three columns
print(x2[:2, :3])
# All rows and every other columns
print(x2[:3, ::2])
# Reversing the subarray dimensions
print(x2[::-1, ::-1])

# Accessing array rows and columns
# First Column of x2
print(x2[:, 0])
# First row of x2
print(x2[0, :])

# Sub-Arrays as no copies view
# Note: Array Slices return views rather than copies of the data, unlike list slicing which return the copies.
print(x2)
x2_sub = x2[:2, :2]
print(x2_sub)
# Modifying the x2_sub array the original array will be changed, this is the default behaviour.
x2_sub[0,0] = 99
print(x2)

# Create copies of arrays
x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)
# If we modify this array the original array will not be changed
x2_sub_copy[0,0] = 10
print(x2_sub_copy)
print(x2)

# 4. Reshaping of arrays
# Below script will put the number 1 to 9 in a 3x3 grid
grid = np.arange(1, 10).reshape((3,3))
print(grid)

# Note: The size of the intial array must eb the size of the reshaped array.
# The reshape method will use the no copy view of the initial array, but with non-contigous memory buffers
# Reshaping can be done to convert the one-dimensional array to two-dimensional row or column matirx.
# This can be done using the reshape or the newaxis method.

x = np.array([1,2,3])
# row vector via reshape
x.reshape((1,3))
"""
o/p:
array([[1, 2, 3]])
"""
# row vector via newaxis
x[np.newaxis, :]
"""
o/p:
array([[1, 2, 3]])
"""

# column vector via reshape
x.reshape((3,1))
"""
o/p:
array([[1],
       [2],
       [3]])
"""

# column vector via newaxis
print(x[:, np.newaxis])
"""
o/p:
[[1]
 [2]
 [3]]
"""

# 5. Array Concatenattion and Splitting

# Concatenation of arrays(np.concatenate, np.vstack, np.hstack)
x = np.array([1,2,3])
y = np.array([3,2,1])
np.concatenate((x,y))
"""
o/p:
array([1, 2, 3, 3, 2, 1])
"""

# Concatenating 2 arrays at once
z = [99, 99, 99]
print(np.concatenate((x,y,z)))
"""
o/p:
[ 1  2  3  3  2  1 99 99 99]
"""

# Two Dimensional Arrays
grid = np.array([
    [1,2,3],
    [4,5,6]
])
print(grid)
# Concatenate along the first axis (vertically)
np.concatenate([grid, grid])
"""
o/p:
array([[1, 2, 3],
       [4, 5, 6],
       [1, 2, 3],
       [4, 5, 6]])
"""
# Concatenate along the second axis (horizontally)
# Note: bdefault concatenation occurs along axis =0, axis =1 is secondary axis
np.concatenate([grid, grid], axis=1)
"""
o/p:
array([[1, 2, 3, 1, 2, 3],
       [4, 5, 6, 4, 5, 6]])
"""

# vstack and hstack
x = np.array([1,2,3])
grid = np.array([
    [9,8,7],
    [6,5,4]
])
# vertically stack the arrays
np.vstack((x, grid))
"""
Output:
array([[1, 2, 3],
       [9, 8, 7],
       [6, 5, 4]])
"""
# horizontally stack the arrays
y = np.array([[99],
              [99]])
np.hstack([grid, y])
"""
Output:
array([[ 9,  8,  7, 99],
       [ 6,  5,  4, 99]])
"""
# Note: np.dstack will stack arrays along the third axis

# Splitting of Arrays - np.split, np.hsplit, np.vsplit
# split- 3 arrays and position of split
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

grid = np.arange(16).reshape((4,4))
print(grid)

# vertical split of multi dimensional array into 2
upper,lower = np.vsplit(grid, [2])
print(upper)
print(lower)

# horizontal split of multi dimensional array
left, right = np.hsplit(grid, [2])
print(left)
print(right)

# Note: np.dsplit() will split arrays along the third axis

