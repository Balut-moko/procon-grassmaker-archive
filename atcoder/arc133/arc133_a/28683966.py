from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
tmp = a[0]
for i in range(n):
    if tmp < a[i]:
        tmp = a[i]
    elif tmp == a[i]:
        continue
    else:
        break
ans = [val for val in a if val != tmp]
print(*ans)
