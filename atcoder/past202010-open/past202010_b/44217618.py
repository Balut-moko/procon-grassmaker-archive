from sys import stdin

readline = stdin.readline
x, y = map(int, readline().split())

if y == 0:
    print("ERROR")
    exit()

ans = x / y + 0.0001
priod = str(ans).find(".")
print(str(ans)[: priod + 3])
