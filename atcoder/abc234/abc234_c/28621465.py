from sys import stdin

readline = stdin.readline
n = int(readline())
n_bin_str = str(bin(n))
print(str(bin(n))[2:].replace("1", "2"))
