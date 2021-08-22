import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

x = np.array([2, 1, 4, 3, 5])
print(selection_sort(x))

def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x

x = np.array([2, 1, 4, 3, 5])
print(bogosort(x))

# Fast Sorting in NumPy
x = np.array([2, 1, 4, 3, 5])
print(np.sort(x))

# In Place Sorting
x.sort()
print(x)

# Argsort method returns the indices of the sorted elements
x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
print(i)

# Sorting along the rows or columns
rand = np.random.RandomState(42)