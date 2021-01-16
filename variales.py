# 1. Class variable / Static variable
# 2. Instance Variable

class Test():
    cls_var = 5  # Class variable / Static variable

    def __init__(self):
        # instance variables
        self.name = 'Abc'
        self.age = 10


obj = Test()
obj.name = 'Ankur'
obj.age = 20

print(obj.name, obj.age, obj.cls_var)
Test.cls_var = 6
print(obj.cls_var)
