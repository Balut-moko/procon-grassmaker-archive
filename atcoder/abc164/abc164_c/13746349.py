def resolve():
    N = int(input())
    S = [input() for i in range(N)]
    S = list(set(S))
    print(len(S))
resolve()