if __name__ == "__main__":  
  # Creation of lists
  list_one = []
  list_two = []

  # User input code
  user_sequence = int(input('Enter an unsigned integer (or -1 to finish): '))

  # While loop to gather list_one
  while user_sequence != -1:
   list_one.append(user_sequence)
   user_sequence = int(input('Enter an unsigned integer (or -1 to finish): '))

  # For loop to calculate cumulative frequency of list one
  cumulative_sum = 0
  for number in list_one:
    if number != -1:
      cumulative_sum += number
      list_two.append(cumulative_sum)
    else:
      break

  # Print second list
  for numbers in list_two:
    print(numbers)
