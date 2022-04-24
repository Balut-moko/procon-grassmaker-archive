from sys import stdin


readline = stdin.readline
n = int(readline())
t = list(map(int, readline().split()))
ans = 0
digit = -1
for val in t:
    if digit < val + 1:
        ans = 1 << val
    elif digit == val + 1:
        ans >>= val
        ans <<= val
        ans += 1 << (val + 1)
    else:
        ans >>= val
        tmp = 0
        if ans % 2 == 1:
            tmp = 1
        ans <<= val
        ans += 1 << val + tmp

    digit = ans.bit_length()


print(ans)
