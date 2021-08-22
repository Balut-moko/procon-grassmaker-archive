from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
s = list(map(int, readline().split()))
t = list(map(int, readline().split()))
if 1 not in s and 1 in t:
    ans = -1
elif 0 not in s and 0 in t:
    ans = -1
else:
    ans = 0
    tmp = s[0]
    left, right = 0, 0
    for i in range(n):
        if s[i] != tmp:
            right = i
            break
    for i in range(n):
        if s[n - i - 1] != tmp:
            left = i + 1
            break
    swap_cost = min(left, right)
    flg = False
    for i in range(m):
        if t[i] == tmp:
            ans += 1
        else:
            tmp = t[i]
            if flg:
                ans += 2
            else:
                ans += swap_cost + 1
                flg = True
print(ans)
