if __name__ == "__main__":
  #Your code goes here. The first line should start at the same column as this one
  weight = int(input('Enter your weight in kilograms>'))
  height = int(input('Enter your height in centimetres>'))
  bmi = weight / (height/100)**2
  print('Your BMI is', bmi )