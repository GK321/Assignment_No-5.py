#Challenge Number:- 1
# # # Problem statement: Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be public. This problem can be broken down into two tasks:
# # # Task 1:  Implement a constructor to initialize the values of three properties: x, y, and z.
# # # Task 2:  Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.
# # # Sample properties 1, 3, 5
# # # Sample method output 35

class Point:                      ##construction of point class
  def __init__(self, x, y, z):    ##implementation of constructor
    self.x = x
    self.y = y
    self.z = z

  def sqSum(self):
    a = self.x
    b = self.y
    c = self.z
    x = a*a
    y = b*b
    z = c*c

    sum = f'SQUARED SUM OF GIVEN NUMBERS IS: {x+y+z}'
    return sum

obj = Point(1,3,5)

print(obj.sqSum())