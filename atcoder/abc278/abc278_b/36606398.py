from sys import stdin


def check(h, m):
    a = h // 10
    b = h % 10
    c = m // 10
    d = m % 10
    b, c = c, b

    hh = a * 10 + b
    mm = c * 10 + d
    if 0 <= hh < 24 and 0 <= mm < 60:
        return True
    return False


readline = stdin.readline
h, m = map(int, readline().split())

while not check(h, m):
    m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
print(h, m)
