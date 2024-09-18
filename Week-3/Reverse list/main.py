if __name__ == "__main__":
  # reverse a list DL (modified by DRS)  ERRONEOUS!
  my_list = ['a', 'b', 'c', 'd']
  print('The original list is ', my_list)

  # The loop iterates up until the halfway point to prevent the loop from re-iterating swapping elements already swapped. 'a' and 'd' are swapped for each other only once as well as 'b' and 'c'.
  
  i = 0
  length = len(my_list)
  half_len = length // 2
  while i < half_len:
    temp = my_list[length - 1 - i]
    my_list[length - 1 - i] = my_list[i]
    my_list[i] = temp
    i += 1
  print('The reversed list is ', my_list)