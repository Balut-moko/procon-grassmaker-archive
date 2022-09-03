from sys import stdin

readline = stdin.readline
s = readline()[:-1]
choice = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for i, val in enumerate(choice):
    if s == val:
        print(5 - i)
