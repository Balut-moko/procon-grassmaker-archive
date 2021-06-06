#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    city = [[] for _ in range(n)]
    for a, b in ab:
        city[a - 1].append(b - 1)
    ans = 0
    for i, c in enumerate(city):
        stack = []
        for val in c:
            stack.append(val)
        visited = [0] * n
        visited[i] = 1
        tmp = 1
        while stack:
            x = stack.pop()
            if visited[x] == 0:
                visited[x] = 1
                for e in city[x]:
                    stack.append(e)
                tmp += 1
        ans += tmp
    print(ans)


if __name__ == "__main__":
    main()
