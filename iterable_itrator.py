''' 
An iterator is an object that contains a countable number of values.
Lists, tuples, dictionaries, and sets are all iterable objects.
All these objects have a iter() method which is used to get an iterator:

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.
'''

ll = [10,11,13,14]

it = iter(ll)

print(it.__next__())
print(it.__next__())

for i in it:
    print(i)


class MyIterator:

    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

obj = MyIterator()

print(obj.__next__())

for i in obj:
    print(i)
