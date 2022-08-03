from sys import stdin

readline = stdin.readline
s = readline()[:-1]

ss = s.replace("x", "")

if ss != ss[::-1]:
    print(-1)
    exit()

left = 0
right = len(s) - 1
ans = 0
while left < right:
    if s[left] == s[right]:
        left += 1
        right -= 1
    else:
        ans += 1
        if s[left] == "x":
            left += 1
        else:
            right -= 1
print(ans)
