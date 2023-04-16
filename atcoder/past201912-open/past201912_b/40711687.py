from sys import stdin

readline = stdin.readline
n = int(readline())
a = [int(readline()) for _ in [0] * n]
pre = a[0]
for val in a[1:]:
    d = val - pre
    if d == 0:
        print("stay")
    elif d < 0:
        print(f"down {-d}")
    else:
        print(f"up {d}")
    pre = val
