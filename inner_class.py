class Parent(): # Outer Class
    def __init__(self, name, age, child_name, child_age):
        self.name = name
        self.age = age
        self.child = self.Child(child_name, child_age)

    class Child(): # Inner Class
        def __init__(self, child_name, child_age):
            self.child_name = child_name
            self.child_age = child_age


obj = Parent('Andrew', 28, 'James', 7)

print(obj.name, obj.age, obj.child.child_name, obj.child.child_age)
