if __name__ == "__main__":
  # Input command
  age = int(input('Your age: '))

  # Railfare
  if age<16 or age>59:
    print('Fare is 120')
  elif age>=16 and age<=59:
    print('Fare is 150')