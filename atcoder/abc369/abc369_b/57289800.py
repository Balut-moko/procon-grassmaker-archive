N = int(input())
AS = [list(input().split()) for _ in [0] * N]

ans = 1 << 60
for l in range(1, 101):
    for r in range(1, 101):
        L = l
        R = r
        tmp = 0
        for a, s in AS:
            a = int(a)
            if s == "L":
                tmp += abs(L - a)
                L = a
            else:
                tmp += abs(R - a)
                R = a
        ans = min(ans, tmp)

print(ans)
