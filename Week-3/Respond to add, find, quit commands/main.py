if __name__ == "__main__":
  # Create lists for test 1 and test 2
  commands_test_one = ['add add','add find','add cat','add bat','add smart','add tart','find add','find find','find cat','find bat','find smart','find tart']
  commands_test_two = ['add house','add house','add shed','add hovel','find house','find shed','find hovel']
  list_of_words = []
  list_of_words_two = []

  # User input code
  user_input = str(input('Enter your command: '))

  # Split input words for test 1 and test 2
  for user_input in commands_test_one:
    command_one = user_input.split()[0]

  for user_input in commands_test_two:
    command_two = user_input.split()[0]

  # Responding differently to 'add' and 'find' commands
  # Test 1
    if command_one == 'add':
      word = user_input[len('add '):]
      list_of_words.append(word)
    elif command_one == 'find':
      find_find = user_input[len('find '):]
      find_found = [word for word in list_of_words if find_find in word]
      for found_find in find_found:
        print(found_find)

    elif command == 'quit':
      break

  # Test 2
    if command_two == 'add':
      word_2 = user_input[len('add '):]
      list_of_words_two.append(word_2)
    elif command_two == 'find':
      find_find_2 = user_input[len('find '):]
      find_found_2 = [word_2 for word_2 in list_of_words_two if find_find_2 in word_2]
      for found_find_2 in find_found_2:
        print(found_find_2)
    elif command_two == 'quit':
      break
