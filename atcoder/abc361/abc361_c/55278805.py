from collections import deque


N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ans = 1 << 60
cnt = 0

q = deque()
for val in A:
    q.append(val)
    # 追加した要素に応じた処理
    cnt += 1
    while q and not (cnt <= N - K):  # (満たすべき条件)
        rm = q.popleft()
        # 取り除いた要素に応じた処理
        cnt -= 1
    # 何らかの処理 右端の要素から左に延ばせる最大の長さ
    if cnt == N - K:
        ans = min(ans, q[-1] - q[0])

print(ans)
