#!/usr/bin/env python3

import sys

def validate_number(n):
    try:
        # Check if valid number
        int(n)

        # Check for leading zeros
        if int(n)!=str(int(n)):
            exit(43)
    except ValueError:
        exit(43)

def check_radius(r):
    r = int(r)
    validate_number(r)

    if r < 0 or r > 1000: 
        exit(43)

def check_cord(c):
    c = int(c)
    validate_number(c)

    if c < -1000 or c > 1000: 
        exit(43)

x1, y1, r1 = input().split()
x2, y2, r2 = input().split()

# Check firste circle
check_cord(x1)
check_cord(y1)
check_radius(r1)

# Check second circle
check_cord(x2)
check_cord(y2)
check_radius(r2)

exit(42)
