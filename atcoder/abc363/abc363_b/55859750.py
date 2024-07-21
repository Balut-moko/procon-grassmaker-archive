N, T, P = map(int, input().split())
L = list(map(int, input().split()))

L.sort()

for i in range(101):
    cnt = 0
    for p in L:
        if p + i >= T:
            cnt += 1
    if cnt >= P:
        print(i)
        exit()
