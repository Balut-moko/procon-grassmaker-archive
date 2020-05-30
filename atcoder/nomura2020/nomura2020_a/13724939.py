def resolve():
    H1, M1, H2, M2, K = map(int, input().split())
    import datetime
    AwakeTime = (H2*60 + M2)-(H1*60 + M1)
    ans = AwakeTime -K
    print(ans)
resolve()