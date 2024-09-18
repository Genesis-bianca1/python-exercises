# Incorrect Function:
#def badswap(a,b):
#  temp = a
#  a = b
#  b = temp

# No values are returned
# Correct code uses 'return' to affect the variables outside the function (when function is called):

# Corrected Function:
def badswap(a,b):
  return b,a  #Simply switch the order of a & b

if __name__ == "__main__":
  x = 1
  y = 2
  badswap(x,y)
  print('x = ',x)
  print('y = ',y)