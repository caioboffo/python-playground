
X = set('spam')      # Make a set out of a sequence in 2.X and 3.X
Y = {'h', 'a', 'm'}  # Make a set with set literals in 3.X and 2.7

print X, Y           # A tuple of two sets without parenthesis

print X & Y          # Intersection
print X | Y          # Union
print X - Y          # Difference
print X > Y          # Superset
