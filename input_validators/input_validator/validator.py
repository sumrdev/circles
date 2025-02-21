import sys
def check_num(a, is_coord):
    try:
        int(a)
        if int(a)!=str(int(a)): exit(43)
        if is_coord and a < -1000: exit()
        if a > 1000: exit(43)
        if a < 0: exit(43)
    except ValueError:
        exit(43)

x1,y1,r1,x2,y2,r2 = map(int, input().split())

if sys.stdin.readline() != "": exit(43)


