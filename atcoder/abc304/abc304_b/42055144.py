from sys import stdin

readline = stdin.readline
n = int(readline())
if n < 1000:
    print(n)
    exit()
digit = len(str(n))
digit -= 3

print(n - n % 10**digit)
