from sys import stdin

readline = stdin.readline
n = int(readline())
c = list(map(int, readline().split()))
q = int(readline())

odd_min = min([c[i] for i in range(n) if i % 2 == 0])
if n > 1:
    even_min = min([c[i] for i in range(n) if i % 2 == 1])
else:
    even_min = 1 << 60
s = 0
z = 0
ans = 0
for _ in range(q):
    que = list(map(int, readline().split()))

    if que[0] == 1:
        x = que[1] - 1
        a = que[2]
        if x % 2 == 0:
            if c[x] - s - z >= a:
                ans += a
                c[x] -= a
                odd_min = min(odd_min, c[x])
        else:
            if c[x] - z >= a:
                ans += a
                c[x] -= a
                even_min = min(even_min, c[x])
    elif que[0] == 2:
        a = que[1]
        if odd_min - s - z >= a:
            s += a
    else:
        a = que[1]
        if odd_min - s - z >= a and even_min - z >= a:
            z += a
print(ans + s * ((n + 1) // 2) + z * n)
