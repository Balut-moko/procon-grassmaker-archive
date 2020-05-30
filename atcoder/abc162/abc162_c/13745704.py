def resolve():
    import math
    K = int(input())
    
    ans = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            gcd1 = math.gcd(a,b)
            for c in range(1, K+1):
                gcd2 = math.gcd(gcd1,c)
                ans += gcd2
    print(ans)
resolve()