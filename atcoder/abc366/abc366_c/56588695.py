from collections import defaultdict


Q = int(input())

dic = defaultdict(int)
kind = 0
for _ in range(Q):
    command, *x = map(int, input().split())
    if command == 1:
        x = x[0]
        dic[x] += 1
        kind += dic[x] == 1
    if command == 2:
        x = x[0]
        dic[x] -= 1
        kind -= dic[x] == 0
    if command == 3:
        print(kind)
