class GrandParent():

    def feature1(self):
        print('feature1')

    def feature2(self):
        print('feature2')


class Parent():

    def __init__(self):
        print('Constructor of PARENT')

    def feature3(self):
        print('feature3')

    def feature4(self):
        print('feature4')


class Child(Parent):  # Single or Multilevel Inheritance

    def __init__(self):
        # super().__init__()
        print('Constructor of CHILD')

    def feature5(self):
        print('feature5')

    def feature6(self):
        print('feature6')


class GrandChild(Child, Parent):  # Multiple Inheritance

    def __init__(self):
        super().__init__() # This will call left to itself only (Methiod Resolution Order) like in this only CHild and Grandchild __init__ will call not Parent one
        print('Constructor of GrandChild')

    def feature7(self):
        print('feature7')


# child_obj = Child()
gran_child = GrandChild()



# obj.feature3()

# print(isinstance(obj, Parent))

# print(issubclass(Child, Parent))
