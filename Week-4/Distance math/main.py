import math

def distance(x1,y1,x2,y2):
  dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
  return dist

if __name__=="__main__":
  x1 = (float(input('Enter value: ')))
  y1 = (float(input('Enter value: ')))
  x2 = (float(input('Enter value: ')))
  y2 = (float(input('Enter value: ')))
  equation = distance(x1,y1,x2,y2)
  print(equation)