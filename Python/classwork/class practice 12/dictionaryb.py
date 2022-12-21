"""
My_list={
    "Applewatch":"babal",
     "price":20000,
    "brand":"branded"
}



class Coordinates:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return f"Coord(x={self.x}, y={self.y})"


  def __sub__(self, other):
    new_x = self.x - other.x
    new_y = self.y - other.y
    return Coordinates(new_x, new_y)

  def distance(self, other):
    6
"""

int =-20
print("the absolute value of -20 is:",abs(int))