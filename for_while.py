'''
for and while
'''

L = [10,20,30]

for i in L:
    print("i :",i)
    print("i :",i)
    print("i :",i)
    print("i :",i)


# In b/n if we want to stop

for i in L:
    print("i :",i)
    if i ==20: # stop for loop
        break


# In b/n if we want to send for next iteration

for i in L:
    if i == 20:
        continue # goto next iteration 
    print("i :",i)
    print("i :",i)
    print("i :",i)
    print("i :",i)



#for-else
for i in L: # fo will execute for all the elements
    print("i :",i)
else: # will execute one time
    print("In Else")


#for-else-break    
for i in L: # fo will execute for all the elements
    print("i :",i)
    break
else: # will execute one time
    print("In Else")

# break will comeout from for and else block both


a = 0
while a < 10:
    print("a : ",a)
    a = a +1

# while
# while-break
# while-continue
# while-break
    


