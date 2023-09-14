from collections import deque


n = int(input())
a = list(map(int, input().split()))
q = deque()
v_xor, v_sum = 0, 0
ans = 0
cnt = 0
for i, val in enumerate(a):
    q.append(val)
    # 追加した要素に応じた処理
    v_xor ^= val
    v_sum += val
    cnt += 1
    while q and not (v_xor == v_sum):  # (満たすべき条件)
        rm = q.popleft()
        # 取り除いた要素に応じた処理
        v_xor ^= rm
        v_sum -= rm
        cnt -= 1
    # 何らかの処理 右端の要素から左に延ばせる最大の長さ
    ans += cnt

print(ans)
