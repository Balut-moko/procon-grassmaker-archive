from sys import stdin


def increment(from_num_li):
    n = len(from_num_li)
    for i in range(n - 1, 0, -1):
        cur = from_num_li[i]
        nxt = from_num_li[i - 1]
        if cur < 9 and abs(cur + 1 - nxt) <= 1:
            from_num_li[i] += 1
            for j in range(i + 1, n):
                from_num_li[j] = max(0, from_num_li[j - 1] - 1)
            return from_num_li
    top = from_num_li[0]
    if top < 9:
        from_num_li[0] += 1
        for j in range(1, n):
            from_num_li[j] = max(0, from_num_li[j - 1] - 1)
        return from_num_li
    from_num_li = [1]
    for i in range(n):
        from_num_li.append(0)
    return from_num_li


readline = stdin.readline
k = int(readline())
num_li = [0]
for i in range(k):
    num_li = increment(num_li)

print(*num_li, sep="")
