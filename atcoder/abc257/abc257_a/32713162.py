from sys import stdin

readline = stdin.readline
n, x = map(int, readline().split())
div, mod = divmod(x, n)

if div == 0:
    print("A")
else:
    if mod == 0:
        print(chr(64 + div))
    else:
        print(chr(65 + div))
