"""
The file lets us understand how data in the array is stored and manipulated.
"""
# 1. Python Code tp sum 100 integers
result = 0
for i in range(100):
    result+=i
print(result)

# 2. Python List
# List of integer values
L = list(range(10))
print(L)

# List of strings
L1 = [str(c) for c in L]
print(L1)

# Heterogeneous List
L2 = [True, "2", 3.0, 4]
print(L2)

# 3. Fixed Type Arrays in Python
import array
L = list(range(10))
A = array.array('i', L)
print(A)
# o/p: array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])-> i: integers

# 4. Creating Array from python lists using numpy
import numpy as np
# integer array
np.array([1,4,5,6])
# o/p: array([1, 4, 5, 6])

# Note: If type of the array does not match NumPy will upcast.
np.array([3.14, 1, 4, 5])
# o/p: array([3.14, 1.  , 4.  , 5.  ])

# Explicit set the data type using the dtype
np.array([1,2,4,5], dtype='float32')
# o/p: array([1., 2., 4., 5.], dtype=float32)

# Nested List result in multi-dimensional arrays
# Explanation: for every number in the list create a list of range
np.array([range(i, i + 3) for i in [2, 4, 6]])

"""
o/p:
array([[2, 3, 4],
       [4, 5, 6],
       [6, 7, 8]])
"""

# 5. Creating Arrays from Scratch

# Create a length-10 integer array filled with zeros
# shape=10, dtype=int
np.zeros(shape=10, dtype=int)
# o/p: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Creating a 3x5 floating point array filled with ones
np.ones(shape=(3,5), dtype=float)
"""
o/p:
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])
"""

# Create an array filled with 3.14(3 by 5 array)
np.full(shape=(3,5),fill_value=3.14)
"""
o/p:
array([[3.14, 3.14, 3.14, 3.14, 3.14],
       [3.14, 3.14, 3.14, 3.14, 3.14],
       [3.14, 3.14, 3.14, 3.14, 3.14]])
"""

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
np.arange(0,20,2)
"""
o/p:
array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
"""

# Create an array of five values evenly spaced between 0 and 1
np.linspace(0,1,5)
"""
o/p:
array([0.  , 0.25, 0.5 , 0.75, 1.  ])
"""

# Create 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random(size=(3,3))
"""
o/p:
array([[0.38139368, 0.84923875, 0.09776632],
       [0.11785315, 0.17929876, 0.85385834],
       [0.63235425, 0.94605426, 0.44374357]])
"""

# Create a 3x3 array of normally distributed random values
# with a mean of 0 and std. deviation 1
np.random.normal(0, 1, size=(3, 3))
"""
o/p:
array([[-0.78391159,  1.13673665, -0.02746491],
       [-1.22399278, -1.35221949, -0.36210907],
       [-0.23539228, -0.15931413,  0.49530479]])
"""

# Create a 3x3 array of random integers between the interval [0,10)
np.random.randint(0, 10, size=(3, 3))
"""
o/p:
array([[1, 3, 0],
       [0, 0, 3],
       [4, 8, 9]])
"""

# Create a 3x3 identity matrix
np.eye(3)
"""
o/p:
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
"""

# Create an uninitialized array of 3 integers
np.empty(3)
"""
o/p:
array([1., 1., 1.])
"""







