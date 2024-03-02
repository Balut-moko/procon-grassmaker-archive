def check(x):
    str_x = str(x)
    if str_x == str_x[::-1]:
        return True
    return False


N = int(input())
ans = 1
x = 1
while x * x * x <= N:
    if check(x * x * x):
        ans = x * x * x
    x += 1

print(ans)
