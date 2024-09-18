if __name__ == "__main__":
  weight = int(input('Please insert the weight of the package in grams: '))
  length = int(input('Please insert the length of the package in centimeters: '))
  diameter = int(input('Please insert the diameter of the package in centimeters: '))
  length_diameter = length + (diameter*2)

  if weight<= 2000 and length <= 90 and length_diameter <= 104:
    print('Yes')
  else:
    print('No')
