# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b),
        a, b = b, a+b

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# by adding this
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

# you can make the file usable as a script as well as an importable module,
#  because the code that parses the command line only runs if the
# module is executed as the 'main' file:
# python 'fibo.py' 50 through the termina for example