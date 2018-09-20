#! /usr/bin/env python

import random

L = {random.randint(1,25)}

while ( L.__len__() < 15 ):
    L.add(random.randint(1,25))

print L


