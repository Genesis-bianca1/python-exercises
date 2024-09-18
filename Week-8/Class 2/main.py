# Adder class and its methods
class Adder:
  def __init__(self):
    self.total = 0
  
  #two other methods
  def add(self,n):
    self.total += n

  def get_total(self):
    return self.total