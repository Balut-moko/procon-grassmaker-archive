import string
from sys import stdin

readline = stdin.readline
s = readline()[:-1]
for val in s:
    if val in string.ascii_lowercase:
        print("error")
        exit()
print(int(s) * 2)
