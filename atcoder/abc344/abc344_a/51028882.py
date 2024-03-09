S = input()

cnt = 0
ans = ""
for val in S:
    if val == "|":
        cnt += 1
    if val != "|" and cnt != 1:
        ans += val
print(ans)
