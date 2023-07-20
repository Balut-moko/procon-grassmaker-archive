from sys import stdin

readline = stdin.readline
t = int(readline())

for _ in range(t):
    n, k = map(int, readline().split())
    cnt = 0
    m = 40
    while n > 0:
        if 3**m <= n:
            n -= 3**m
            cnt += 1
        else:
            m -= 1
    ans = "No"
    if cnt <= k and k % 2 == cnt % 2:
        ans = "Yes"
    print(ans)
