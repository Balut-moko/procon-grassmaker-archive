def resolve():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print(1)
    else:
        ans = int((H*W+1)/2)
        print(ans)
resolve()
