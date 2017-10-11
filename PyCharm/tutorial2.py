x = 4
def example3():
    # what we do here is defined x as a global variable.
    global x
    # now we can:
    print(x)
    x+=5
    print(x)
example3()

x = 5
def example4():
    globx = x
    # now we can:
    print(globx)
    globx+=5
    print(globx)
example4()

x = 6
def example(modify):
    print(modify)
    modify += 5
    print(modify)
    return modify

x = example(x)
print(x)

import calculator
#import subtraction from calculator
print (dir(calculator))
calc = calculator.calculator()
adds = calc.addition
adds(1,2)
calc.addition(1,3)

#x = input('What is your name?: ')
#print('Hello',x)


import statistics
from statistics import mean as m
example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]
x = m(example_list)
print(x)
y = statistics.median(example_list)
print(y)
z = statistics.mode(example_list)
print(z)
a = statistics.stdev(example_list)
print(a)
b = statistics.variance(example_list)
print(b)

import examplemod
examplemod.ex('test')

print(
'''
This
is
a
test 
'''
    )

print(
'''
So it works like a multi-line
comment, but it will print out.

You can make kewl designs like this:

==============
|            |
|            |
|    BOX     |
|            |
|            |
==============
'''
    )

exNum1 = -5
exNum2 = 5
print(abs(exNum1))
if abs(exNum1) == exNum2:
    print('True!')

#help()

import time
# will work in a typical installation of Python, but not in the embedded editor
#help(time)

exList = [5,2,1,6,7]

largest = max(exList)
print(largest)

smallest = min(exList)
print(smallest)

x = 5.622
x = round(x)
print(x)

y = 5.256
y = round(y)
print(y)

# Converting data types:

# Converting a string to an integer:
intMe = '55'
intMe = int(intMe)
print(intMe)

# Converting and integer to a string:
stringMe = 55
stringMe = str(stringMe)
print(stringMe)

# Converting an integer to a float:
floatMe = 55
floatMe = float(floatMe)
print(floatMe)

import os
curDir = os.getcwd()
print(curDir)
'''
The above code will get your current working directory, hence "cwd."
To make a new directory:
'''
os.mkdir('newDir')
# To change the name of, or rename, a directory:
os.rename('newDir','newDir2')
# To remove a directory:
os.rmdir('newDir2')

import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

#def main(arg):
    #print(arg)

#main(sys.argv[1])