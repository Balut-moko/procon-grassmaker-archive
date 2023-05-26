from sys import stdin

readline = stdin.readline
H, W = map(int, readline().split())


def cut_rectangle(h, w):
    mex_h = h // 2
    sh1 = mex_h * w
    sh2 = (h - mex_h) * w
    if sh2 < sh1:
        sh1, sh2 = sh2, sh1
    return sh1, sh2


ans = 1 << 60
for i in range(2):
    if i:
        H, W = W, H
    for h in range(1, H):
        h1 = H - h
        h2 = h
        s1 = h1 * W
        s2 = h2 * W
        if s2 < s1:
            s1, s2 = s2, s1
            h1, h2 = h2, h1
        s3, s4 = cut_rectangle(h2, W)
        s5, s6 = cut_rectangle(W, h2)
        if s6 - s5 < s4 - s3:
            s3, s4 = s5, s6
        tmp = max(s1, s3, s4) - min(s1, s3, s4)
        ans = min(ans, tmp)

print(ans)
