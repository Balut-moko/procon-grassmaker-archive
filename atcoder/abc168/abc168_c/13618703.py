def resolve():
    import math
    A, B, H, M = map(int, input().split())
    Hradian = math.radians(30*H+M/2)
    Mradian = math.radians(6*M)
    Hx, Hy = -1*A*math.sin(Hradian), A*math.cos(Hradian)
    Mx, My = -1*B*math.sin(Mradian), B*math.cos(Mradian)
    ans = ((Hx-Mx)**2 + (Hy-My)**2)**0.5
    print(ans)
resolve()