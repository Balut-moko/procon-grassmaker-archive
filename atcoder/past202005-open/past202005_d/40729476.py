from sys import stdin

readline = stdin.readline
N = int(readline())
s = [readline()[:-1] for _ in [0] * 5]

templete = [
    ".###..#..###.###.#.#.###.###.###.###.###.",
    ".#.#.##....#...#.#.#.#...#.....#.#.#.#.#.",
    ".#.#..#..###.###.###.###.###...#.###.###.",
    ".#.#..#..#.....#...#...#.#.#...#.#.#...#.",
    ".###.###.###.###...#.###.###...#.###.###.",
]


ans = ""
for n in range(N):
    for num in range(10):
        for i in range(5):
            for j in range(4):
                if s[i][4 * n + j] != templete[i][4 * num + j]:
                    break
            else:
                continue
            break
        else:
            ans += str(num)
print(ans)
