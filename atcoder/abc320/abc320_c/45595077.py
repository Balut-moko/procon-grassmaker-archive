m = int(input())
s1 = input()
s2 = input()
s3 = input()
INF = 1 << 60
ans = INF

for i in range(310):
    for j in range(310):
        if i == j:
            continue
        for k in range(310):
            if i == k or j == k:
                continue
            if s1[i % m] == s2[j % m] == s3[k % m]:
                ans = min(ans, max(i, j, k))

print(ans if ans != INF else -1)
