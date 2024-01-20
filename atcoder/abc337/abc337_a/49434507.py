N = int(input())
XY = [tuple(map(int, input().split())) for _ in [0] * N]
t = 0
a = 0

for x, y in XY:
    t += x
    a += y

if t > a:
    print("Takahashi")
elif t < a:
    print("Aoki")
else:
    print("Draw")
