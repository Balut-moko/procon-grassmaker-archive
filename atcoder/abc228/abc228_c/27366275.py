from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
p = [[i, sum(map(int, readline().split()))] for i in range(n)]
rank = sorted(p, reverse=True, key=lambda x: x[1])
border = rank[k - 1][1]

for i in range(n):
    if p[i][1] + 300 >= border:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)
