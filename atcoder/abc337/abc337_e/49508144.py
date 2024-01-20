N = int(input())
for m in range(N):
    cnt = 2**m
    if N <= cnt:
        break

print(m, flush=True)


def has_bit(n, i):
    return n & (1 << i) > 0


juice = [[] for _ in range(m)]
for i in range(1 << m):
    for j in range(m):
        if has_bit(i, j):
            if i + 1 <= N:
                juice[j].append(i + 1)

for i in range(m):
    a = [len(juice[i])] + juice[i]
    print(*a, flush=True)

res = input()
ans = 1
for i in range(m):
    if res[i] == "1":
        ans += 1 << i

print(ans)
