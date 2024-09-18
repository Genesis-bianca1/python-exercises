if __name__ == "__main__":
  # A program to calculate the total number of beans in a can, given the user input and three different options:
  blackbeans_input = int(input('Enter number of black beans in can: '))
  whitebeans_input = int(input('Enter number of white beans in can: '))
  beans_in_can = blackbeans_input + whitebeans_input

  # Allowed operations:
  print('Your allowed operations are:')
  
  if blackbeans_input >=2:
    print('BB pick out two black beans')

  if  whitebeans_input >=2:
    print('WW pick out two white beans')

  if blackbeans_input >=1 and whitebeans_input >=1:
    print('BW pick out one white and one black beans')
  
  option = input('Enter your option: ')

  # Options and their operations code
  if option == 'BB':
    blackbeans_now = (blackbeans_input-2) + 1
    print('After the operation there are:')
    print(blackbeans_now,' black beans')
    print(whitebeans_input,' white beans')
  elif option == 'WW':
    whitebeans_now = whitebeans_input-2
    blackbeans_now = blackbeans_input+1
    print('After the operation there are: ')
    print(blackbeans_now,' black beans')
    print(whitebeans_now,' white beans')
  elif option == 'BW':
    bothbeans_now = blackbeans_input-1
    print('After the operation there are: ')
    print(bothbeans_now,' black beans')
    print(whitebeans_input,' white beans')