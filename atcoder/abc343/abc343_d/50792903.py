from collections import defaultdict


N, T = map(int, input().split())

di = defaultdict(int)
di[0] = N
score_set = set()
score_set.add(0)
cnt = 1
scores = [0] * (N + 1)
for i in range(T):
    A, B = map(int, input().split())
    di[scores[A]] -= 1
    if di[scores[A]] == 0:
        score_set.discard(scores[A])
        cnt -= 1
    scores[A] += B
    di[scores[A]] += 1
    if di[scores[A]] == 1:
        score_set.add(scores[A])
        cnt += 1
    print(cnt)
