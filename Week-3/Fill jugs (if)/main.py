if __name__ == "__main__":
  # A program asking the user for the capacity and volume of two jugs
  A_capacity = int(input('What is the capacity of jug A? '))
  B_capacity = int(input('What is the capacity of jug B? '))
  A_volume = int(input('How many litres are in jug A? '))
  B_volume = int(input('How many litres are in jug B? '))

  # Displaying selection of operations
  print('Operations are:')
  print('FA - fill jug A from tap')
  print('FB - fill jug B from tap')
  print('EA - empty jug A')
  print('EB - empty jug B')
  print('AB - transfer as much water as possible from jug A to jug B')
  print('BA - transfer as much water as possible from jug B to jug A')

  operation = input('Which operation would you like to perform? ')
  
  # Code for operations
  print('After your operation, there are: ')
  
  if operation == 'FA':
    print(A_capacity,' litres in A and',B_volume,' litres in B')
  elif operation == 'FB':
    print(A_volume,' litres in A and',B_capacity,' litres in B')
  elif operation == 'EA':
    print(0,' litres in A',B_volume,' litres in B')
  elif operation == 'EB':
    print(A_volume,' litres in A and',0,' litres in B')
  elif operation == 'AB':
    new_A_volume = A_volume - min(B_capacity - B_volume, A_volume)
    full_B_jug = B_volume + min(B_capacity - B_volume, A_volume)
    print(new_A_volume,' litres in A and',full_B_jug,' litres in B')
  elif operation == 'BA':
    full_A_jug = A_volume + min(A_capacity - A_volume, B_volume)
    new_B_volume = B_volume - min(A_capacity - A_volume, B_volume)
    print(full_A_jug,' litres in A and',new_B_volume,' litres in B')