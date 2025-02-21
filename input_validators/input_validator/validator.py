#!/usr/bin/python3

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
    validate_number(r)

    if r < 0 or r > 1000: 
            exit(43)

def check_cord(c):
    validate_number(c)

    if c < -1000 or c > 1000: 
            exit(43)

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

# Check firste circle
check_cord(x1)
check_cord(y1)
check_radius(r1)

# Check second circle
check_cord(x2)
check_cord(y2)
check_radius(r2)

if sys.stdin.readline() != "": exit(43)

exit(42)
