#!/usr/bin/python3
import random

# Read the second... arguments as ints Example call:
# example.py {seed} 1 2 3 4
x1,y1,r1,x2,y2,r2 = [random.randint(-1000,1000), random.randint(-1000,1000), random.randint(0,1000), random.randint(-1000,1000), random.randint(-1000,1000), random.randint(0,1000)]

# Print in standard format, i.e. one line with the number of values,
# followed by the space-separated values.
print(x1,y1,r1,x2,y2,r2)
