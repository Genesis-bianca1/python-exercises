import numpy as np


#Function returns True if arr represents a magic square, otherwise False
def is_magic_square(arr):

# Counts all rows and columns of array
  row, col = arr.shape
  
# If n rows != n columns, arr is not a matrix square
  if row != col:
    return False

# If sum of each column != sum of each row
  if not np.all(arr.sum(axis=0) == arr.sum(axis=1)):
    return False

  return True

if __name__ == "__main__":
  magic = np.array([[2,7,6],[9,5,1],[4,3,8]])
  print("Applying is_magic_square to")
  print(repr(magic))
  print("Result = ",is_magic_square(magic))

  non_magic = np.array([[2,6,7],[9,5,1],[4,3,8]])
  print("Applying is_magic_square to")
  print(repr(non_magic))
  print("Result = ",is_magic_square(non_magic))