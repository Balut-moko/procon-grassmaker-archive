def resolve():
    import math
    a, b = input().split()
    num = int(a+b)
    ans = (num**0.5)%1
    if ans == 0:
        print('Yes')
    else:
        print('No')
resolve()