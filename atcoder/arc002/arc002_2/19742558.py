#!/usr/bin/env python3
import datetime


def main():
    d = input()
    day = datetime.datetime.strptime(d, '%Y/%m/%d')
    while True:
        if day.year % (day.month * day.day) == 0:
            print(day.strftime('%Y/%m/%d'))
            break
        day += datetime.timedelta(days=1)


if __name__ == "__main__":
    main()
