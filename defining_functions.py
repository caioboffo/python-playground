# This file show how to define functions and parameters in python
#
# To define a function in python use the keyword 'def'
#


def f(a, b, c):
    print(a, b, c)


# Matching parameters by position
f(1, 2, 3)


# Matching parameters by name
f(c=3, b=2, a=1)

# Matching parameters by position and name
f(1, c=3, b=2)


# While defining a function with defaults do this
def f(a, b=2, c=3):
    print(a, b, c)


# Then you could call the function like this
f(1)

f(a=1)

f(1, 4)

f(1, c=3)


# Arguments as a tuple
def f(*args):
    print(args)


f()

f(1)

f(1, 2, 3, 4)


# Arguments as a dictionary
def f(**args):
    print(args)


f()

f(a=1, b=2)


# Multiple definitions
def f(a, *pargs, **kargs):
    print(a, pargs, kargs)


f(1, 2, 3, x=1, y=2)

# Unpacking arguments

def func(a, b, c, d):
    print(a, b, c, d)

args = (1, 2)
args += (3, 4)
func(*args)


args = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
func(**args)
# should print only values not keys

"""
if sometest:
   action, args = func1, (1,)
else:
   action, args = func2, (1, 2, 3)
...etc...
action(*args)
"""


