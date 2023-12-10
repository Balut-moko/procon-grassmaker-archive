K, G, M = map(int, input().split())

Ga, Ma = 0, 0

for _ in range(K):
    if Ga == G:
        Ga = 0
    elif Ma == 0:
        Ma = M
    else:
        if Ma + Ga <= G:
            Ga += Ma
            Ma = 0
        else:
            Ma -= G - Ga
            Ga = G

print(Ga, Ma)
