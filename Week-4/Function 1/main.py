def prod3(n1,n2,n3):
  factors = n1*n2*n3
  return factors

if __name__ == "__main__":
  n1 = float(input('Enter a number: '))
  n2 = float(input('Enter a number: '))
  n3 = float(input('Enter a number: '))
  n = prod3(n1,n2,n3)
  print(n)
  