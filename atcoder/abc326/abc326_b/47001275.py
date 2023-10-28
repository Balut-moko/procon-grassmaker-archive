def check(N):
    N = str(N)
    if int(N[-3]) * int(N[-2]) == int(N[-1]):
        return True
    return False


N = int(input())

while True:
    if check(N):
        print(N)
        exit()
    N += 1
