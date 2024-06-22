N = int(input())
S = [input() for _ in [0] * N]

print(sum(1 if s == "Takahashi" else 0 for s in S))
