from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

ans = s.count("#")
tmp = ans
for val in s[::-1]:
    if val == ".":
        tmp += 1
    else:
        tmp -= 1
    ans = min(ans, tmp)
print(ans)
