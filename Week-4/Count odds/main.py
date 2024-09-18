def count_odds(numlist):
  odds = 0
  for num in numlist:
    if num%2 != 0:
      odds +=1
  return odds

if __name__=="__main__":
  user_input = input("Enter a list of values separated by comma: ")
  split_list = [int(n) for n in user_input.split(",")]
  num_of_odds = count_odds(split_list)
  print(num_of_odds)