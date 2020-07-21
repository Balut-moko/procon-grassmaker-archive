from collections import deque


def main():
    da = deque(input())
    db = deque(input())
    dc = deque(input())

    card = da.popleft()

    while True:
        if card == "a":
            if len(da) != 0:
                card = da.popleft()
            else:
                ans = "A"
                break
        elif card == "b":
            if len(db) != 0:
                card = db.popleft()
            else:
                ans = "B"
                break
        elif card == "c":
            if len(dc) != 0:
                card = dc.popleft()
            else:
                ans = "C"
                break
    print(ans)


if __name__ == "__main__":
    main()