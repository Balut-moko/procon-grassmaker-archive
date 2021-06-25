from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
hole = sum(a)
a = a + a
left, right = 0, 1
tmp = sum(a[left:right])
ans = 'No'
while left < n and right < 2 * n:
    if tmp * 10 < hole:
        tmp += a[right]
        right += 1
    elif hole < tmp * 10:
        tmp -= a[left]
        left += 1
    else:
        ans = 'Yes'
        break
print(ans)
