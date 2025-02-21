#!/usr/bin/python3

from random import random
import sys

random.seed(sys.argv[1])

x1,y1,r1 = [random.randint(-1000,1000), random.randint(-1000,1000), random.randint(0,1000)]
x2,y2,r2 = [random.randint(-1000,1000), random.randint(-1000,1000), random.randint(0,1000)]

print(x1, y1, r1)
print(x2, y2, r2)
