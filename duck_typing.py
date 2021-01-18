''' 
Duck typing is a concept related to dynamic typing, 
where the type or the class of an object is less important
than the methods it defines. When you use duck typing, 
you do not check types at all. Instead, you check for 
the presence of a given method or attribute.

Ex -  If there is a bird and that bird behaves like a duck 
then it walks like a duck it quack like a duck and it
swin like a duck, it should be a duck.
'''


class Duck():

    def duck(self):
        print('Orignal Duck')


class Bird():

    def duck(self):
        print('Act like a Duck')


class DuckBehaviour():

    def check_duck(self, obj):
        obj.duck()


class NotDuck():

    def diff_method():
        print('Not a Duck')


duck_checker = DuckBehaviour()

obj = Duck()

obj1 = Bird()

obj3 = NotDuck()

duck_checker.check_duck(obj)

duck_checker.check_duck(obj1)

duck_checker.check_duck(obj3)
