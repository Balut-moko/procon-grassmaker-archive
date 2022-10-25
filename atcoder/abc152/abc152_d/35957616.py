from sys import stdin

readline = stdin.readline
n = int(readline())

n_digit = len(str(n))
cnt = [[0] * 10 for _ in range(10)]
for a in range(1, n + 1):
    start = int(str(a)[0])
    end = a % 10
    cnt[start][end] += 1

ans = 0
for a_s in range(1, 10):
    for a_e in range(1, 10):
        ans += cnt[a_s][a_e] * cnt[a_e][a_s]
print(ans)
