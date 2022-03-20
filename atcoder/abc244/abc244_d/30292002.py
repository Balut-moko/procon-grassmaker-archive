from sys import stdin

readline = stdin.readline

s = list(readline().split())
t = list(readline().split())
ans = "Yes"
for i in range(3):
    if i == 0:
        tmp = [s[1], s[0], s[2]]
        if tmp == t:
            ans = "No"
    elif i == 1:
        tmp = [s[2], s[1], s[0]]
        if tmp == t:
            ans = "No"
    else:
        tmp = [s[0], s[2], s[1]]
        if tmp == t:
            ans = "No"
print(ans)
