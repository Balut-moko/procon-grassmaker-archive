def main():
    C = int(input())
    NML = [sorted(map(int, input().split())) for c in range(C)]
    Nmax = 1
    Mmax = 1
    Lmax = 1
    for nml in NML:
        Nmax = max(Nmax, nml[0])
        Mmax = max(Mmax, nml[1])
        Lmax = max(Lmax, nml[2])
    print(Nmax * Mmax * Lmax)


if __name__ == "__main__":
    main()
