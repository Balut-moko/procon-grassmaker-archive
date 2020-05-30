def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    import collections
    c = collections.Counter(A)
    for i in range(1,N+1):
        print(c[i])
resolve()