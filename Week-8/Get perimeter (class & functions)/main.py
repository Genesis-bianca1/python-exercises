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

  def get_perimeter(self):
    return 2 * (self.width + self.height)

class Circle(Shape):
  def __init__(self,xcen,ycen,radius):
    super().__init__(xcen,ycen)
    self.radius = radius

  def get_area(self):
    return math.pi * self.radius**2

  def get_diameter(self):
    return 2 * self.radius

  def get_perimeter(self):
    return 2 * math.pi * self.radius

        
    