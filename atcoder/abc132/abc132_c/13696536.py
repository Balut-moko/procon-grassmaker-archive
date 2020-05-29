def resolve():
    N = int(input())
    d = list(map(int, input().split()))
    
    d.sort()
    if d[int(N/2-1)] < d[int(N/2)]:
        ans = len(range(d[int(N/2-1)], d[int(N/2)]))
    else:
        ans = 0
    print(ans)
resolve()