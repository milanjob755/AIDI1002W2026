# STEP 1: Import NumPy
import numpy as np
 
# STEP 2: Create NumPy Arrays
 
 
# 1D Array
arr1 =np.array([10,20,30,40])
print(arr1)
# 2D Array (Matrix)
arr2 = np.array([
  [1,2,3],
  [4,5,6]
 ])
print(arr2)
# Array using built-in functions
zeros_arr = np.zeros(5,dtype=int)
print(zeros_arr)
zeros2_arr = np.zeros((2,3))
print(zeros2_arr)
ones_arr = np.ones(5,dtype=int)
print(ones_arr)
range_arr = range_arr = np.arange(1,10,2)
print(range_arr)
linspace_arr = np.linspace(0,1,5)
print(linspace_arr)
print(linspace_arr.shape)
 
# STEP 3: Print Arrays and Their Properties
 
 
# STEP 4: Indexing and Slicing
print("first Element:",arr1[0])
print("last Element:",arr1[-1])
 
print("elements from 1 to 3:",arr1[1:3])
print("Second Column of 2 dimentional array",arr2[:,1])

 
# STEP 5: Mathematical Operations
print("add:",arr1+5)
print("Multiply:",arr1)
print("Square:",arr1 **2)
 
# STEP 6: Statistical Operations
print("sum:",arr1.sum())
print("Mena:",arr1.mean())
print("ma:",arr1.max())
# STEP 7: Reshaping Arrays
reshaped = arr1.reshape(2,2)
print(reshaped)
# STEP 8: Comparison and Boolean Operations
print("Elements greater than 20:",arr1[arr1 > 20])
print(arr1 > 20)
 
# STEP 9: Array Aggregation (Row-wise / Column-wise)

print("ColumnWiseSum:",arr2.sum(axis=0))
print("RowWiseSum:",arr2.sum(axis=1))