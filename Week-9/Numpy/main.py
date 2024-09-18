import numpy as np


def squares(lower,upper):
  numbers = np.arange(lower,upper)
  squares = numbers**2
  return squares

if __name__ == "__main__":
  #Illustration of how squares would be called
  print("squares 0 to 9")
  #The repr function returns a representation of an array
  #That makes clear that it is an array rather than a list
  sqr = squares(0,10)
  print(repr(sqr))