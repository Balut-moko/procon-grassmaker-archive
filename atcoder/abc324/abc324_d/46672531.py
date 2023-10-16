N = int(input())
S = list(input())
S.sort()

ans = 0
for i in range(4 * 10**6):
    val = list(str(i * i))
    val.extend(["0"] * (N - len(val)))
    val.sort()
    if S == val:
        ans += 1


print(ans)
