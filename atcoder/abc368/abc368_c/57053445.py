N = int(input())
H = list(map(int, input().split()))

T = 0
for h in H:
    d, m = divmod(h, 5)
    T += d * 3
    h -= d * 5
    while h > 0:
        T += 1
        if T % 3 == 0:
            h -= 3
        else:
            h -= 1


print(T)
