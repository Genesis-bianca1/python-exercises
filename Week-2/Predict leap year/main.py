if __name__ == "__main__":
  # Input command
  year = int(input('Enter year: '))
  
  # Code to distinguish leap year from common year
  if year%4 == 0:
    print (year,' is a leap year.')
  elif year%4 == 0 and year%400 != 0 and year%100 != 0 and year%400 == 0:
    print (year,' is a leap year.')

  if year%100 == 0 and year%400 != 0 and year%4 != 0:
    print (year,' is a common year.')
  elif year%400!= 0:
    print (year,' is a common year.')
  