from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
t = readline()[:-1]

for i in range(n):
    if s[i] == t[i]:
        continue
    if s[i] == "1" and t[i] == "l":
        continue
    if s[i] == "l" and t[i] == "1":
        continue
    if s[i] == "0" and t[i] == "o":
        continue
    if s[i] == "o" and t[i] == "0":
        continue
    print("No")
    exit()
print("Yes")
