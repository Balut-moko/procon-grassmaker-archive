from sys import stdin


def max_num(n_str):
    res = list(n_str)
    for i in range(3):
        if res[i] != '9':
            res[i] = '9'
            break
    return ''.join(res)


def min_num(n_str):
    res = list(n_str)
    if res[0] != '1':
        res[0] = '1'
    elif res[1] != '0':
        res[1] = '0'
    elif res[2] != '0':
        res[2] = '0'
    return ''.join(res)


readline = stdin.readline
a, b = readline().split()
print(max(int(max_num(a)) - int(b), int(a) - int(min_num(b))))
