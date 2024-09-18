if __name__ == "__main__":
  eggs = int(input("How many eggs do you have?>"))
  dozen = eggs // 6
  leftover = eggs % 6
  print('You have', eggs, 'egg/s which is', dozen, 'dozen/s and', leftover, 'leftover/s.')