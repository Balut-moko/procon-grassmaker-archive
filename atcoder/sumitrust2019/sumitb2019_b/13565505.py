def resolve():
    import math
    N = int(input())
    price = N/1.08
    reTaxprice1 = math.floor(math.floor(price)*1.08)
    reTaxprice2 = math.floor(math.ceil(price)*1.08)
    if reTaxprice1 == N:
        print(math.floor(price))
    elif reTaxprice2 == N:
        print(math.ceil(price))
    else:
        print(':(')
resolve()