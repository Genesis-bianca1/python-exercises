if __name__ == "__main__":
  # List of powers of 2
  powers_list = [2**i for i in range(0,11)]

  # Specify index start point
  index = 1
  # The len() command to count the items in a list
  # While index is less than the items in the list(10 items), print vertical list.
  while index < len(powers_list):
    index += 1
    print(powers_list[index-1])