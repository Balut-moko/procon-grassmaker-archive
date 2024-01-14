N = int(input())


def ten2baseInt(value, base):
    """
    10進数からn進数へ変換
    """
    if int(value // base):
        return ten2baseInt(int(value // base), base) + str(value % base)
    return str(value % base)


N -= 1
li = list(ten2baseInt(N, 5))
d = {"0": 0, "1": 2, "2": 4, "3": 6, "4": 8}
li = [d[v] for v in li]

print(*li, sep="")
