from sys import stdin

readline = stdin.readline
n = int(readline())
digit = len(str(n))
ans = 0

for i in range(1, digit + 1):
    for j in range(digit):
        left = int('1' * i + '0' * j)
        right = int('1' * (i - 1) + '2' + '0' * j)
        if right <= n:
            ans += right - left
        elif left <= n:
            ans += n - left + 1
        else:
            break
print(ans)
