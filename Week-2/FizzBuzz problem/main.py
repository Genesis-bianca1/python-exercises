if __name__ == "__main__":
  number = int(input('Enter an integer: '))
if number%3 == 0 and number%5 != 0:
  print('Fizz')
elif number%5 == 0 and number%3 != 0:
  print ('Buzz')
else: 
  if number%3 == 0 and number%5 == 0:
    print('Fizz Buzz')
  else:
    print(number)