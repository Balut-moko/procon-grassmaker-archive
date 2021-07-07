from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))

r = 0
ans = 0
tmp = 0
kinds = 0
num_dict = dict()
for i in range(n):
    while r < n and kinds <= k:
        tmp += 1
        if a[r] not in num_dict:
            num_dict[a[r]] = 1
            kinds += 1
        else:
            num_dict[a[r]] += 1
        r += 1
    if i == r:
        r += 1
    else:
        if k < kinds:
            num_dict[a[i]] -= 1
            tmp -= 1
            if num_dict[a[i]] == 0:
                del num_dict[a[i]]
                kinds -= 1
    ans = max(ans, tmp)
print(ans)
