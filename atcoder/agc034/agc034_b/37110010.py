from sys import stdin

readline = stdin.readline
s = readline()[:-1]
right = len(s) - 1
cnt = 0
ans = 0
while right >= 0:
    if right > 1 and s[right] == "C" and s[right - 1] == "B":
        cnt += 1
        right -= 2
    elif s[right] == "A":
        ans += cnt
        right -= 1
    else:
        right -= 1
        cnt = 0

print(ans)
