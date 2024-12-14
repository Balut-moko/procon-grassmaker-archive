from collections import deque


N, S = map(int, input().split())
A = list(map(int, input().split()))

S %= sum(A)

A = A + A

flag = False
cnt = 0

q = deque()
for val in A:
    q.append(val)
    # 追加した要素に応じた処理
    cnt += val
    while q and not (cnt <= S):  # (満たすべき条件)
        rm = q.popleft()
        # 取り除いた要素に応じた処理
        cnt -= rm
    # 何らかの処理 右端の要素から左に延ばせる最大の長さ
    if cnt == S:
        flag = True

print("Yes" if flag else "No")
