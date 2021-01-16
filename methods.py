'''
1. Instance Method
2. Class Method
3. Static Method '''


class Student():
    school_name = 'GBSSS No-2'  # class or static variable

    def __init__(self, student_name, age, marks):  # instace method
        self.student_name = student_name
        self.age = age
        self.marks = marks

    def show(self):
        print(self.student_name, self.age, self.marks)
        

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @staticmethod
    def info():
        print('School is build in 1989')


Student.info()

print(Student.get_school_name())

s1 = Student('JAMES', 14, 89)
s1.show()
s2 = Student('Williams', 14, 87)
s2.show()

# print(s1.student_name, s1.age, s1.marks)
# print(s2.student_name, s2.age, s2.marks)