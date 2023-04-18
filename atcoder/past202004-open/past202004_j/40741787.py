from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def f(s):
    if "(" not in s:
        return s
    l, r = 0, 0
    for i, val in enumerate(s):
        if val == "(":
            l = i
        if val == ")":
            r = i
            t = s[l + 1 : r]
            return f(s[:l] + t + t[::-1] + s[r + 1 :])


readline = stdin.readline
s = readline()[:-1]
print(f(s))
