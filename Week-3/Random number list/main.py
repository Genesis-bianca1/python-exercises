import random

if __name__ == "__main__":

# Complete list and list of numbers > 50  
  complete_list = [57, 71, 92, 62, 30, 49, 6, 42, 78, 62]
  greater_equal_50 = [num for num in complete_list if num >= 50]
  
  print('Complete list: ',complete_list,' of which: ',greater_equal_50,' are >= 50')

# Random numbers from complete_list
  list_one = []
# Random numbers from greater_equal_50
  list_two = []

# Pick 10 numbers from each list
for n in range(10):
  number_1 = random.choice(complete_list)
  number_2 = random.choice(greater_equal_50)

# Store random numbers in their corresponding list
  list_one.append(number_1)
  list_two.append(number_2)
  
print('list one: ',list_one, 'list two',list_two)