def change_length(length, factor):
  length = length * factor
  print("The new length is now", length)
  return length
  if __name__ == "__main__":
      length = 10
      factor = 2
      change_length(length, factor)
      print("length after applying the factor is", length)