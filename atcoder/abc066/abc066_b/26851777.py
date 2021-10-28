from sys import stdin


def check(s):
    if len(s) % 2 == 1:
        return False
    h = len(s) // 2
    for i in range(h):
        if s[i] != s[h + i]:
            return False
    return True


readline = stdin.readline
s = readline()[:-1]
n = len(s)
for i in range(1, n):
    tmp = s[:n - i]
    if check(tmp):
        break

print(len(tmp))
