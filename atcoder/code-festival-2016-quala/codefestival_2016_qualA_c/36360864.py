from sys import stdin

readline = stdin.readline
s = list(readline()[:-1])
k = int(readline())

for i, val in enumerate(s):
    if val == "a":
        continue
    cnt = 26 - ord(val) + ord("a")
    if cnt <= k:
        s[i] = "a"
        k -= cnt

k %= 26
s[-1] = chr(ord(s[-1]) + k)

print(*s, sep="")
