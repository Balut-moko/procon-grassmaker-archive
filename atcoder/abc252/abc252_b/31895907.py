from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))
b = set(map(lambda x: int(x) - 1, readline().split()))

max_a = max(a)
ans = "No"
for i, val in enumerate(a):
    if val == max_a and i in b:
        ans = "Yes"
print(ans)
