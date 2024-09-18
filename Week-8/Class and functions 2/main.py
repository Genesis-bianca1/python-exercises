import math

class Shape:
  def __init__(self,xcen,ycen):
    self.xcen = xcen
    self.ycen = ycen
        
  def move(self,dx,dy):
    self.xcen += dx
    self.ycen += dy
    
class Rectangle(Shape):
  def __init__(self,xcen,ycen,width,height):
    super().__init__(xcen,ycen)
    self.width = width
    self.height = height
        
  def get_area(self):
    return self.width * self.height
    
  def is_inside(self,x,y):
    left = self.xcen - self.width/2
    right = self.xcen + self.width/2
    low = self.ycen - self.height/2
    top = self.ycen + self.height/2
    return x > left and x < right and y > low and y < top

class Circle(Shape):
  def __init__(self,xcen,ycen,radius):
    super().__init__(xcen,ycen)
    self.radius = radius

  def get_area(self):
    return math.pi * self.radius**2

  def get_diameter(self):
    return 2 * self.radius

  def is_inside(self,x,y):
    coordinate = (x - self.xcen)**2 + (y - self.ycen)**2 
    return coordinate < self.radius**2