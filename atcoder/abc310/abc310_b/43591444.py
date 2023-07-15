from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * n]
ans = "No"
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i][0] < a[j][0]:
            continue
        i_set = set()
        j_set = set()
        for k in range(a[i][1]):
            i_set.add(a[i][k + 2])
        for k in range(a[j][1]):
            j_set.add(a[j][k + 2])

        if i_set != i_set & j_set:
            continue
        if a[i][0] > a[j][0] or len(j_set - i_set) > 0:
            ans = "Yes"
print(ans)
