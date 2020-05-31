def resolve():
    li = input().split()
    A = int(li[0])
    B = int(li[1].replace('.',''))
    ans = int(A*B//100)
    print(ans)
resolve()