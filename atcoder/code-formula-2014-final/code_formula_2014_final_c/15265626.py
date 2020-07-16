def main():
    import re
    S = input()
    user = re.findall(r'@[a-z]+', S)
    user = list(set(user))
    user.sort()
    for u in user:
        print(u[1:])


if __name__ == "__main__":
    main()