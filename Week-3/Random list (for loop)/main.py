import random

if __name__ == "__main__":
  print('Pick a number between 0 and 99 (inclusive)')
  random_list =[]
  
  index = 0
  for index in range(1,9):
    random_var = random.randint(0,99)
    index_appended = random_list.append(random_var)
    print(random_list[index-1])