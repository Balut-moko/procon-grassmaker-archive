from sys import stdin

readline = stdin.readline
x = int(readline())
print('Yes' if x != 0 and x % 100 == 0 else 'No')
