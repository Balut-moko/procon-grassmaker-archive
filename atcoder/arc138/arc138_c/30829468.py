from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a_sorted = sorted(a)
a_rad = a_sorted[n // 2]
b = []
for i in range(n):
    if a[i] < a_rad:
        b.append(1)
    elif a[i] > a_rad:
        b.append(-1)
    else:
        b.append(0)

b_cs = [0] * (n + 1)
for i in range(n):
    b_cs[i + 1] = b_cs[i] + b[i]

k = b_cs.index(min(b_cs))
s = sum(a_sorted[n // 2 :])
print(k, s)
