from sys import stdin

readline = stdin.readline
k = int(readline())
div, mod = divmod(k, 60)

hh = str(21 + div).zfill(2)
mm = str(mod).zfill(2)
print(f"{hh}:{mm}")
