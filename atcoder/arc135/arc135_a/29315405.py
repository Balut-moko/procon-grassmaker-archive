from sys import stdin

readline = stdin.readline
x = int(readline())
mod = 998244353
tmp = 1
cnt = 0
while tmp < x:
    tmp *= 2
    cnt += 1
if tmp - x < x - (tmp // 2):
    exp_3 = tmp - x
    exp_2 = tmp // 2 - exp_3 * 2
else:
    exp_3 = x - (tmp // 2)
    exp_2 = tmp // 4 - exp_3
ans = 1 * pow(2, exp_2, mod) * pow(3, exp_3, mod) % mod
print(ans)
