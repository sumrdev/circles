import math
x1,y1,r1,x2,y2,r2 = map(int, input().split())
d = math.hypot(x2-x1,y2-y1)
if( d < r1 + r2):
    xr = r1 *r1
    yr = r2 *r2

    if d<=abs(yr-xr):
        print(math.pi * min(xr,yr))
        exit(0)
    t1 = 2 * math.acos(xr + d * d - yr) / (2 * d * r1)
    t2 = 2 * math.acos(yr + d * d - yr) / (2 * d * r2)

    print(0.5 * (xr *  (t1 - math.sin(t1))) + yr * (t2 - math.sin(t2)))
    exit(0)

print(0)
