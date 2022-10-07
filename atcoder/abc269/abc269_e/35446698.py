from sys import stdin

readline = stdin.readline
n = int(readline())


def count_rook(a, b, c, d):
    print(f"? {a} {b} {c} {d}", flush=True)
    return int(readline())


def search_rook_row(a, b):
    while a < b:
        mid = (a + b) // 2
        if count_rook(a, mid, 1, n) == mid - a:
            b = mid
        else:
            a = mid + 1
    return b


b = search_rook_row(1, n)


def search_rook_col(c, d):
    while c < d:
        mid = (c + d) // 2
        if count_rook(1, n, c, mid) == mid - c:
            d = mid
        else:
            c = mid + 1
    return d


d = search_rook_col(1, n)

print(f"! {b} {d}", flush=True)
