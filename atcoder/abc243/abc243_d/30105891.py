from sys import stdin

readline = stdin.readline

n, x = map(int, readline().split())

s = readline()[:-1]

depth = 0

while 2**depth <= x:

    depth += 1

depth -= 1

side = x - 2**depth

if x % 2 == 0:

    now = "L"

else:

    now = "R"

for val in s:

    if val == "U":

        depth -= 1

        if depth < 79:

            side //= 2

    if val == "L":

        depth += 1

        if depth < 80:

            side *= 2

    if val == "R":

        depth += 1

        if depth < 80:

            side = side * 2 + 1

    if val != "U":

        now = val

ans = 2**depth + side

print(ans)

