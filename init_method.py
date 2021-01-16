'''__init__ method
"__init__" is a reseved method in python classes. 
It is called as a constructor in object oriented terminology. 
This method is called when an object is created from a class 
and it allows the class to initialize the attributes or
instance variable of the class'''


''' self
The word 'self' is used to represent the instance of a class. 
By using the "self" keyword we access the attributes and 
methods of the class in python.'''


class Rectangle:
    def __init__(self, length, breadth, unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost

    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost


r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s sq units" % (r.get_area()))
