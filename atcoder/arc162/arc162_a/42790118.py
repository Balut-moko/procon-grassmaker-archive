from sys import stdin

readline = stdin.readline
t = int(readline())
for _ in range(t):
    n = int(readline())
    a = list(map(lambda x: int(x) - 1, readline().split()))
    di = {v: i for i, v in enumerate(a)}
    ans = 0
    rank = -1
    for i in range(n):
        if di[i] < i:
            continue
        if rank < di[i]:
            rank = di[i]
            ans += 1

    print(ans)
