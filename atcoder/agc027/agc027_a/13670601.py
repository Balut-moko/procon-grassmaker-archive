def resolve():
    N, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    okashi = 0
    for i in range(N):
        okashi += a[i]
        if okashi > x:
            ans = i
            break
        elif okashi == x:
            ans = i+1
            break
    else:
        ans = N-1
    print(ans)
resolve()