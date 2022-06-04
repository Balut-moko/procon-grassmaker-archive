from sys import stdin


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


readline = stdin.readline
n = int(readline())

sq = [False] * (n + 1)
i = 1
while i * i <= n:
    sq[i * i] = True
    i += 1

d = [[1] for _ in [0] * (n + 1)]
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        d[j].append(i)

cnt = [0] * (n + 1)
for i in range(1, n + 1):
    f = 0
    for j in range(len(d[i])):
        if sq[d[i][j]]:
            f = d[i][j]
    cnt[i // f] += 1

ans = 0
for i in range(n + 1):
    ans += cnt[i] * cnt[i]
print(ans)
