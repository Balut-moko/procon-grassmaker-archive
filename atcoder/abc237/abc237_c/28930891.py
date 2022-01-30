from sys import stdin

readline = stdin.readline
s = list(readline()[:-1])
left, right = 0, 0
for i in range(len(s)):
    if s[i] == "a":
        left += 1
    else:
        break
for i in range(len(s) - 1, -1, -1):
    if s[i] == "a":
        right += 1
    else:
        break
if left < right:
    s = s[: len(s) - (right - left)]
if s == s[::-1]:
    ans = "Yes"
else:
    ans = "No"
print(ans)
