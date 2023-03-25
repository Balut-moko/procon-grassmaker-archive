from sys import stdin

readline = stdin.readline
n = int(readline())
w = list(readline().split())
flag = False
for val in w:
    if val in ["and", "not", "that", "the", "you"]:
        flag = True
print("Yes" if flag else "No")
