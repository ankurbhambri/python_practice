import copy


# Shallow copy

''' A shallow copy creates a new object which stores the reference 
of the original elements. So, a shallow copy doesn't create a copy 
of nested objects, instead it just copies the reference of nested 
objects. This means, a copy process does not recurse or create 
copies of nested objects itself.'''

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

new_list = copy.copy(old_list)

new_list.append([5, 5, 5])
old_list.append([4, 4, 4])

new_list[0][1] = 'b'

print("Old list:", id(old_list), old_list)
print("New list:", id(new_list), new_list)

# Deep Copy

''' A deep copy creates a new object and recursively adds the copies 
of nested objects present in the original elements. '''


old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", id(old_list), old_list)
print("New list:", id(new_list), new_list)
