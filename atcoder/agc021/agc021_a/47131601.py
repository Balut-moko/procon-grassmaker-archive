N = input()
n = len(N)
ans = int(N[0])
flag = False
for i in range(1, n):
    if N[i] != "9" and not flag:
        ans += 9
        ans -= 1
        flag = True
    else:
        ans += 9
print(ans)
