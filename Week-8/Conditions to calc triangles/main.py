# A program using measurements and coordinates of an isosceles triangle

import math

class Shape:
  def __init__(self,xcen,ycen):
    self.xcen = xcen
    self.ycen = ycen
        
  def move(self,dx,dy):
    self.xcen += dx
    self.ycen += dy

#ITriangle is a subclass of class 'Shape'
class ITriangle(Shape):
  def __init__(self,xcen,ycen,base,height):
    super().__init__(xcen,ycen)
    self.base = base
    self.height = height

# Area of triangle
  def get_area(self):
    return self.base * self.height / 2
      
# Perimeter of triangle
  def get_perimeter(self):
    return self.base + math.sqrt(self.base**2 + 4*self.height**2)

# Detects whether the coordinates entered are inside our triangle
  def is_inside(self,x,y):
    distance_x = x - self.xcen
    distance_y = y - (self.ycen - self.height/2)

# Returns True when, otherwise 'False':
    condition_1 = distance_y + self.height > 0
    condition_2 = 2 * self.height * distance_x - self.base * distance_y > 0
    condition_3 = 2 * self.height * distance_x + self.base * distance_y < 0

    return condition_1 and condition_2 and condition_3