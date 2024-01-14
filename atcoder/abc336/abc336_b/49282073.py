N = int(input())
ans = 0
for v in bin(N)[::-1]:
    if v == "0":
        ans += 1
    else:
        break
print(ans)
