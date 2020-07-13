"""
エラトステネスの篩で素数列挙
実行時間

10^2 : 0.00014s
10^3 : 0.000557s
10^4 : 0.007912s
10^5 : 0.156275s
10^6 : 2.370358s
10^7 : 54.244016s

2*10^5くらいまでか
"""

# import math
def getprime(n):
    if not isinstance(n, int):
        raise TypeError("Input int")
    if n == 1:
        return -1
    if n == 2:
        return [2]
    prime = []
    # 約数はsqrt(N)まで調べればOK
    data = [i+1 for i in range(1,n)]
    while True:
        p = data[0]
        if p >= int(n**0.5)+1:
            return prime+data
        prime.append(p)
        # pで割り切れないものだけを残す
        data = [d for d in data if d%p != 0]


if __name__ == "__main__":
    from datetime import datetime as dt
    for i in range(2,7):
        st = dt.now()
        data = getprime(10**i)
        diff = dt.now()-st
        print("10^{} : {}s".format(i,diff.total_seconds()))
