# issubclass(object, subclass)

# Check if the class myObj is a subclass of myAge
class myAge:
  age = 36

class myObj(myAge):
  name = "John"
  age = myAge

x = issubclass(myObj, myAge)