from sys import stdin
import math

readline = stdin.readline
n = int(readline())
p = list(map(int, readline().split()))
num_li = list(range(1, n + 1))

k = 1
cnt = n
for val in p:
    idx = num_li.index(val)
    cnt -= 1
    k += idx * math.factorial(cnt)
    num_li.remove(val)

num_li = list(range(1, n + 1))
k -= 1
ans = []
for i in range(n):
    for val in num_li:
        if k > math.factorial(len(num_li) - 1):
            k -= math.factorial(len(num_li) - 1)
            continue
        ans.append(val)
        break
    num_li.remove(val)
print(*ans)
