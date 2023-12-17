N = int(input())
S = list(map(int, input().split()))

x = [0, 0]
for s in S:
    x.append(s - x[-1] - x[-2])
c1 = -min(x[::3])
c2 = -min(x[1::3])
c3 = min(x[2::3])

if c1 + c2 > c3:
    print("No")
    exit()
a, b = c1, c2
add = [a, b, -a - b]
A = [xi + add[i % 3] for i, xi in enumerate(x)]
print("Yes")
print(*A)
