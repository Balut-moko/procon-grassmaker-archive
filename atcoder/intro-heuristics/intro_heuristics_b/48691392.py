D = int(input())
C = list(map(int, input().split()))
S = [tuple(map(int, input().split())) for _ in [0] * D]
T = [int(input()) - 1 for _ in [0] * D]
last = [0] * 26
score = 0
for i in range(D):
    score += S[i][T[i]]
    last[T[i]] = i + 1
    for j in range(26):
        score -= C[j] * (i + 1 - last[j])
    print(score)
