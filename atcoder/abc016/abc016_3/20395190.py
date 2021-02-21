#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    for i in range(n):
        friends = set(graph[i])
        friends.add(i)
        friendsfriends = set()
        for j in graph[i]:
            for k in graph[j]:
                friendsfriends.add(k)
        print(len(friendsfriends - friends))


if __name__ == "__main__":
    main()
