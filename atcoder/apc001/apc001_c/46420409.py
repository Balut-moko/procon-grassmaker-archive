def question(arg):
    print(arg, flush=True)
    return input()


N = int(input())
res = ""
pre = question(0)
if pre == "Vacant":
    exit()

l, r = 0, N
while res != "Vacant":
    mid = (l + r) // 2
    res = question(mid)
    if pre == res:
        if mid % 2 == 0:
            l = mid
        else:
            r = mid
    else:
        if mid % 2 == 0:
            r = mid
        else:
            l = mid
