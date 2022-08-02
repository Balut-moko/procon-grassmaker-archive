from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

min_ = 0
cnt = 0
for val in s:
    if val == "(":
        cnt += 1
    else:
        cnt -= 1
    min_ = min(min_, cnt)

ans = "(" * -min_ + s + ")" * (-min_ + cnt)
print(ans)
