def main():
    L, X, Y, S, D = map(int, input().split())
    road = abs(S - D)
    road_r = L - abs(S - D)
    speed = X + Y
    speed_r = X - Y
    if speed_r >= 0:
        if S < D:
            ans = road / speed
        else:
            ans = road_r / speed
    else:
        if S < D:
            ans = min(road / speed, road_r / abs(speed_r))
        else:
            ans = min(road_r / speed, road / abs(speed_r))
    print(ans)


if __name__ == "__main__":
    main()
