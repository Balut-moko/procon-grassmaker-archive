from sys import stdin

readline = stdin.readline
s = readline()[:-1]
q = int(readline())
query = [tuple(map(int, readline().split())) for _ in [0] * q]


def g(char, add):
    return chr(ord("A") + (ord(char) - ord("A") + add) % 3)


def f(t, k):
    if t == 0:
        return s[k]
    if k == 0:
        return g(s[0], t)
    return g(f(t - 1, k // 2), (k % 2) + 1)


for t, k in query:
    print(f(t, k - 1))
