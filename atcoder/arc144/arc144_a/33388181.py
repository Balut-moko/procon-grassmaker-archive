from sys import stdin

readline = stdin.readline
n = int(readline())
print(2 * n)
div, mod = divmod(n, 4)
if mod == 0:
    print("4" * div)
else:
    print(str(mod) + "4" * div)
