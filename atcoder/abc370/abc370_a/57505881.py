L, R = map(int, input().split())

if L and not R:
    ans = "Yes"
elif not L and R:
    ans = "No"
else:
    ans = "Invalid"

print(ans)
