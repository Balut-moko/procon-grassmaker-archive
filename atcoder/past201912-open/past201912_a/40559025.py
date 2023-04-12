from sys import stdin
import string

readline = stdin.readline
s = readline()[:-1]

for i in range(3):
    if s[i] in string.ascii_lowercase:
        print("error")
        exit()
print(int(s) * 2)
