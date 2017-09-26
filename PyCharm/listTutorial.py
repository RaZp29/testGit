#Tuples that cannot be changed
def example():
    return 15, 12

x, y = example()
print(x,y)

# in the above case, we have used a tuple and cannot modify it... and
# we definitely do not want to!

x = [1,3,5,6,2,1,6]

'''
You can then reference the whole list like:
'''
print(x)

x[0] = 7
# or a single element by giving its index value.
# index values start at 0 and go up by 1 each time

print(x[0],x[1])

# first we need an example list:
x = [1,6,3,2,6,1,2,6,7]
# lets add something.
# we can do .append, which will add something to the end of the list, like:
x.append(55)
print(x)
#inserts 33 at index 2
x.insert(2,33)
print(x)
#removes the first 6 that is found
x.remove(6)
print(x)

print(x[5])

#returns index of the first 1
print(x.index(1))
#returns number of 1s in the list
print(x.count(1))

x.sort()
print(x)

y = ['Jan','Dan','Bob','Alice','Jon','Jack']
y.sort()
print(y)
y.reverse()
print(y)

#Multi-dimensional lists
x = [[2,6],[6,2],[8,2],[5,12]]
print(x[2])

print(x[2][1])

y = [[5,2],
     [6,2],
     [3,1],
     [12,6]
    ]
print(y)