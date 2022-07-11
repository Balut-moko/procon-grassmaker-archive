from sys import stdin

readline = stdin.readline
sx, sy, tx, ty = map(int, readline().split())

dist_x = tx - sx
dist_y = ty - sy
move1 = "R" * dist_x + "U" * dist_y
move2 = "L" * dist_x + "D" * dist_y

ans = move1 + move2 + "DR" + move1 + "ULUL" + move2 + "DR"
print(ans)
