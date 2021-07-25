from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
b = sorted(map(int, readline().split()))
ans = set()
for i in range(n):
    x = a[0] ^ b[i]
    c = sorted([a[j] ^ x for j in range(n)])
    if b == c:
        ans.add(x)
ans = sorted(list(ans))
print(len(ans))
if len(ans):
    print(*ans, sep='\n')
