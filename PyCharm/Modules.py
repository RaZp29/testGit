print 'Fibonacci'
import fibo

fibo.fib(1000)
print

arr = fibo.fib2(100)
print(arr)
name = fibo.__name__
print(name)

# If you intend to use a function often you can assign it to a local name:
fiba = fibo.fib
fiba(500)
print

from fibo import fib, fib2
fib(500)
print

from fibo import *
fib(500)
print

import sys
print sys.version_info
#sys.ps1
#sys.ps2
#sys.ps1 = 'C> '

# The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:
print dir(fibo)
# Without arguments, dir() lists the names you have defined currently:
# Note that it lists all types of names: variables, modules, functions, etc.
fibs = fibo.fib
print dir()

# dir() does not list the names of built-in functions and variables.
# If you want a list of those, they are defined in the standard module __builtin__
import __builtin__
print dir(__builtin__)