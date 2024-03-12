H, W, A, B = map(int, input().split())

ans = 0


def dfs(i, bit, a, b):
    if i == H * W:
        global ans
        ans += 1
        return
    if bit >> i & 1:
        dfs(i + 1, bit, a, b)
        return
    if b:
        dfs(i + 1, bit | 1 << i, a, b - 1)
    if a:
        if i % W != W - 1 and not bit & 1 << (i + 1):
            dfs(i + 1, bit | 1 << i | 1 << (i + 1), a - 1, b)
        if i + W < H * W:
            dfs(i + 1, bit | 1 << i | 1 << (i + W), a - 1, b)


dfs(0, 0, A, B)
print(ans)
