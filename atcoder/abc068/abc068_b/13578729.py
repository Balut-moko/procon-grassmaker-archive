def resolve():
    N = int(input())
    for i in range(1,9):
        if 2**i > N:
            ans = 2**(i-1)
            break
    print(ans)
resolve()
