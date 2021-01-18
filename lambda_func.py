'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

lambda arguments : expression
'''


def addy(a, b): return a + b
def sqrt(x): return x * x


print(addy(5, 6), sqrt(5))


ll = [2, 3, 4, 5, 6]

''' The map() function executes a specified function for each item in an iterable. 
The item is sent to the function as a parameter. '''

sqrt_all = list(map(lambda a: a*a, ll))

print(sqrt_all)


vv = [1,2,3,4,5]


print('\n'.join(str(vv)))
