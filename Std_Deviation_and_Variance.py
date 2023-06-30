import numpy as np

arr1 = np.array([1,2,4,5])

# Population standard deviation for the array
print(np.std(arr1))

# Population variance of the array
print(np.var(arr1))

# Sample standard deviation for the array
print(np.std(arr1, ddof=1))

# Sample variance of the array
print(np.var(arr1, ddof=1))