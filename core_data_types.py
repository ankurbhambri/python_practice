print("Numbers :")
print("-"*40)
#-------------
a = 10 # Everything is object
a = int(a)
print("a : ",a)

print("-"*40)
#-------------


print("Strings:")
print("-"*40)
#-------------

b = "Python"
c = str("Python")
print("b,c :",b,c)
print("Methods inside the class str is : ")
print(dir(c))

result = c.startswith("Py")
print("result : ",result)

print("Getting substring called slicing")
print("string 1 to 5 : ",c[1:5]) # 1 to 4

print("-"*40)
#-------------

print("list:")
print("-"*40)
#-------------
# more than one element
L = [10,"Python"]
M = list([10,"Python"])

print("List L :",L)
print("Methods inside list class is :")
print(dir(L))

result = L.append(200)
print("list after append 200 is :",result)

print("-"*40)
#-------------

print("tuple :")
print("-"*40)
#-------------

# more than one element - IMMUTABLE
T = (10,"Python")
T2 = tuple((10,"Python")) 

print("Tuple T :",T)
print("Methods inside tuple class is :")
print(dir(T))

result = T.index("Python")
print("Indexof python :",result)


print("-"*40)
#-------------


print("Dictionary :")
print("-"*40)
#-------------
# more than one element

D1 = {"A":10}
D2 =dict({"A":10})

print("Dict are : ",D1,D2)

print("Methods inside the class :")
print(dir(D1))

result = D1.keys()
print("LIst of keys : ",result)

print("-"*40)
#-------------

print("set :")
print("-"*40)
#-------------
# more than one element : UNIQUE VALUES

S1 = {10,10,20,30}
S2 = set({10,10,20,30})

print("sets are : ",S1,S2)

print("Methods inside set")
print(dir(S1))

S1.add(400)
S1.add(400)

print("Set after adding 400 ",S1)

print("-"*40)
#-------------

print("frozeset :")
print("-"*40)
#-------------
# more than one element : UNIQUE VALUES- IMMUTABLE

S1 = frozenset({10,10,20,30,30})
print("S1 :",S1)

print("Methods in frozen set class :")
print(dir(S1))

S2 = frozenset({20,30,40})

result = S1.union(S2)
print("Union of 2 sets are : ",result)

print("-"*40)
#-------------


print("List of Builtin classes/varaibles/functions avaible in python :")
print("-"*40)
#-------------

print(dir(__builtins__))

print("-"*40)
#-------------



a = 100
b = a # Reference copy
a = 200
b = 300

