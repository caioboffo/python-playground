# Keyword-Only Arguments
# Usefull to pass parameter and named parameters as configurations

def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, c=3)
kwonly(a=1, c=3)
kwonly(1, 2, 3) # TypeError kword() missing required keyword-only argument 'c'

def kwonly(a, *, b, c): # this form indicates b and c keyword-only params
    print(a, b, c)

kwonly(1, c=3, b=2)
kwonly(c=3, b=2, a=1)
kwonly(1, 2, 3) # TypeError


# Keyword-Only parameters and default argument

def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)


kwonly(1)
kwonly(1, c=3)
kwonly(1, 2, 3)


# Keyword-only parameters must be coded before the **args
def f(a, *b, c=6, **d): print(a, b, c, d)

f(1, 2, 3, x=4, y=5)
f(1, 2, 3, x=4, y=6, c=7)
f(1, 2, 3, c=7, x=4, y=6)
