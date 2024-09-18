if __name__ == "__main__":
 weight = int(input('Enter your weight>'))
 height = int(input('Enter your height>'))
 bmi = weight/(height/100)**2
print('Your BMI is', bmi)