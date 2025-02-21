import math

x1,y1,r1,x2,y2,r2 = map(int, input().split())

d = math.hypot(x2-x1,y2-y1)

if( d < r1 + r2):
    rr1 = r1 * r1
    rr2 = r2 * r2

    if d<=abs(r2-r1):
        print(math.pi * min(rr1,rr2))
        exit(0)

    t1 = 2 * math.acos((rr1 + d * d - rr2) / (2 * d * r1))
    t2 = 2 * math.acos((rr2 + d * d - rr1) / (2 * d * r2))

    print(0.5 * (rr1 *  (t1 - math.sin(t1))) + rr2 * (t2 - math.sin(t2)))
    exit(0)

print(0)
