"""
This file will helps us understand the need of ufuncs(Universal Functions) provided by NumPy
"""
import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1, 10, size=5)
print(compute_reciprocals(values))
"""
o/p:
[0.16666667 1.         0.25       0.25       0.125     ]
"""

# Note: For big arrays the time taken would have been greater.

# 1. Ufuncs
"""
Statically typed compiled routine, which is a vectorized operation that applies the operation to each element of the 
array.
Vectorized operation in NumPy are implemented using ufuncs.
"""
# Below both the scripts will behave similarly.
print(compute_reciprocals(values))
print(1.0/values)

# UFuncs on multi-dimensional arrays
x = np.arange(9).reshape((3,3))
print(2**x)

# i. Array Arithmetic
x = np.arange(4)
print("x = ", x)
print("x + 5 = ", x+5)
print("x - 5 = ", x-5)
print("x * 2 = ", x*2)
print("x / 2 = ", x/2)
print("x // 2 = ", x//2)
print("-x = ", -x)
print("x ** 2 = ", x**2)
print("x % 2 = ", x%2)
"""
NumPy ufunc for each of the above operations are:
np.add, np.subtract, np.negative, np.multiply, np.divide, np.floor_divide, np.power, np.mod
"""
# ii. Absolute Value
x = np.array([-2, -1, 0, 1, 2])
print(abs(x))
"""
NumPy ufunc
np.absolute/np.abs
"""

# iii. Trignometric Functions
theta = np.linspace(0, np.pi, 3)

print("theta = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

# Inverse Trig functions
x = [-1, 0, 1]
print("x = ", x)
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))

# iv. Exponents and Logarithms
x = [1, 2, 3]
print("x = ", x)
print("e ^ x = ", np.exp(x))
print("2 ^ x = ", np.exp2(x))
print("3 ^ x = ", np.power(3, x))

x = [1, 2, 4, 10]
print("x = ", x)
print("ln(x) = ", np.log(x))
print("log2(x) = ", np.log2(x))
print("log10(x) = ", np.log10(x))

x = [0, 0.001, 0.01, 0.1]
print("exp(x) - 1 =", np.expm1(x))
print("log(1 + x) =", np.log1p(x))



# 2. Specialized Ufuncs
from scipy import special
# Gamma functions(generalized factorials) and related functions
x = [1, 5, 10]
print("gamma(x) = ", special.gamma(x))
print("ln|gamma(x) = ", special.gammaln(x))
print("beta(x, 2) = ", special.beta(x,2))

# Error function, its complement and inverse
x = np.array([0, 0.3, 0.7, 1.0])
print("erf(x)  =", special.erf(x))
print("erfc(x) =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))

# 3. Advanced UFunc Features
# Specifying the output
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out = y)
print(y)

# Note: The above can also be used with the array views as below
y = np.zeros(10)
np.power(2, x, out = y[::2])
print(y)

# 4. Aggregates
"""
reduce an array with reduce method of any ufunc
- A reduce repeatedly applies a given operation to an array until only a single elements remain
"""
x = np.arange(1,6)
print(x)
# o/p: [1 2 3 4 5]
np.add.reduce(x)
# o/p: 15
np.multiply.reduce(x)
# o/p: 120

# To store the intermediate results of the operation we can use accumlate method
np.add.accumulate(x)

# 5. Outer Products
"""
Helps to create a multiplication table
"""
x = np.arange(1, 6)
np.multiply.outer(x, x)
"""
o/p:
array([[ 1,  2,  3,  4,  5],
       [ 2,  4,  6,  8, 10],
       [ 3,  6,  9, 12, 15],
       [ 4,  8, 12, 16, 20],
       [ 5, 10, 15, 20, 25]])
"""
