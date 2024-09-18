if __name__ == "__main__":
  temperature = float(input('Enter the temperature in Celsius: '))
  
  if temperature <= 0:
    print('At ',temperature,' degrees celsius, water is solid')
  elif temperature >= 100:
    print('At ',temperature,' degrees celsius, water is gaseous')
  elif temperature>0 and temperature<100:
    print('At ',temperature,' degrees celsius, water is liquid')
  