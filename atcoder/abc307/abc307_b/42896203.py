from sys import stdin


def check(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


readline = stdin.readline
n = int(readline())
s = [readline()[:-1] for _ in [0] * n]
ans = "No"
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if check(s[i] + s[j]):
            ans = "Yes"

print(ans)
