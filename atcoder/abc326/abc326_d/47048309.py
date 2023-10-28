from itertools import permutations, product

N = int(input())
R = input()
C = input()


def head(s):
    for val in s:
        if val != ".":
            return val


for a, b, c in product(permutations(range(N)), repeat=3):
    if any(ai == bi or bi == ci or ci == ai for ai, bi, ci in zip(a, b, c)):
        continue
    S = [["."] * N for _ in range(N)]
    for i, j in enumerate(a):
        S[i][j] = "A"
    for i, j in enumerate(b):
        S[i][j] = "B"
    for i, j in enumerate(c):
        S[i][j] = "C"

    if "".join(map(head, S)) == R and "".join(map(head, zip(*S))) == C:
        print("Yes")
        print(*map(lambda s: "".join(s), S), sep="\n")
        exit()
print("No")
