

print('Single Quotes')
print('you\'ll have success here')
print("you'll have success here too")
print(2**4)
print(5/2)

condition = 1
while condition < 5:
	print(condition)
	condition += 1

#while True:
    #print('doing stuff!!')

exampleList = [18,25,'cat','moon',2,14]

for x in exampleList:
    print(x)

for x in range(7,11):
    print(x)

def example():
    print('this code will run')
    z = 3 + 9
    print(z)

def simple_addition(num1=2,num2=3):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)

simple_addition(5,3)
simple_addition()

x = 5
y = 10
z = 22

if x > y:
    print('x is greater than y')
elif x > z:
    print('x is greater than z')
else:
    print('if and elif never ran...')

example()

def basic_window(width,height,font='TNR'):
    # let us just print out everything
    print(width,height,font)
basic_window(350,500)