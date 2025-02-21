#!/usr/bin/env python3

import sys


def validate_number(n):
    try:
        # Check if valid number
        int(n)

        # Check for leading zeros
        if n != str(int(n)):
            print("Found leading zeros", n)
            exit(43)
    except ValueError:
        print("Not a number", n)
        exit(43)


def check_radius(r):
    validate_number(r)
    r = int(r)

    if r < 0 or r > 1000:
        print("Out of range (r)", r)
        exit(43)


def check_cord(c):
    validate_number(c)
    c = int(c)

    if c < -1000 or c > 1000:
        print("Out of range (c)", c)
        exit(43)


x1, y1, r1 = input().split()
x2, y2, r2 = input().split()

# Check for no extra garbage in the input file
if sys.stdin.readline() != "":
    print("Found garbage")
    exit(43)

# Check firste circle
check_cord(x1)
check_cord(y1)
check_radius(r1)

# Check second circle
check_cord(x2)
check_cord(y2)
check_radius(r2)

print("Yippie")
exit(42)
