from sys import stdin


def odd_even_sum(n_str):
    digit = len(n_str)
    even, odd = 0, 0
    for i in range(digit):
        if i % 2 == 0:
            odd += int(n_str[i])
        else:
            even += int(n_str[i])
    if digit % 2 == 0:
        even, odd = odd, even
    return even, odd


readline = stdin.readline
print(*odd_even_sum(readline()[:-1]))
